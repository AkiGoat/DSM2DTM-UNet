import numpy as np
# from scipy import interpolate
# import matplotlib.pyplot as plt
from osgeo import gdal
import pandas as pd
# from sklearn.model_selection import train_test_split
# import torch
# import torchvision
# from torch.utils.data import Dataset
# import os
# from tqdm import tqdm, trange


def readTIFF(path, tiff, flag=False):
  data = gdal.Open(path + tiff, gdal.GA_ReadOnly)
  band = data.GetRasterBand(1)
  arr = band.ReadAsArray()
  if flag:
    for i in range(arr.shape[0]):
      for j in range(arr.shape[1]):
        if arr[i][j]>9999:
          arr[i][j]=0.0
    return arr
  else:
    return np.ma.masked_where(arr > 9999, arr)

def normalizeRela(arr):
  arr_mean = np.mean(arr)
  arr_std = np.std(arr)
  return (arr-arr_mean)/arr_std

def slicePic(pic, cut_width, cut_length):
  sliced_pic = []
  width = pic.data.shape[0]
  length = pic.data.shape[1]
  num_width = int(width/cut_width)
  num_length = int(length/cut_length)
  for i in range(0, num_width):
    for j in range(0, num_length):
      # dtm_ = dtm[i*cut_width:(i+1)*cut_width, j*cut_length:(j+1)*cut_length]
      # dsm_ = dsm[i*cut_width:(i+1)*cut_width, j*cut_length:(j+1)*cut_length]
      pic_ = pic[i*cut_width:(i+1)*cut_width, j*cut_length:(j+1)*cut_length]
      # mean_pic_ = np.mean(pic_[:, :, 0])
      # std_pic_ = np.std(pic_[:, :, 0])
      # pic_[:, :, 0] = (pic_[:, :, 0]-mean_pic_)/std_pic_
      sliced_pic.append(pic_)
  return sliced_pic

def augmentateData(pics):
  pics_augmentated = []
  for pic in pics:
    pic_rot90 = np.rot90(pic)
    pic_rot180 = np.rot90(pic, 2)
    pic_rot270 = np.rot90(pic, 3)
    pic_flip = np.fliplr(pic)
    pic_flip_rot90 = np.rot90(pic_flip)
    pic_flip_rot180 = np.rot90(pic_flip, 2)
    pic_flip_rot270 = np.rot90(pic_flip, 3)
    pics_augmentated += [pic_rot90, pic_rot180, pic_rot270, pic_flip, pic_flip_rot90, pic_flip_rot180, pic_flip_rot270]
  return pics_augmentated
  
def generateGroundTruth(dsm, dtm):
  length = dsm.shape[0]
  width = dsm.shape[1]
  mask_ = np.zeros((2, length, width), dtype=bool)
  for i in range(length):
    for j in range(width):
      mask_[0][i][j] = True
      if dsm.mask[i][j] == False:
        if dtm.mask[i][j] == True:
          mask_[1][i][j] = True
          mask_[0][i][j] = False
        elif dsm.data[i][j] - dtm.data[i][j] > 2.0:
          mask_[1][i][j] = True
          mask_[0][i][j] = False
  return mask_

def stackPics(dsm_fill, slope, layer, normalization=True):
  pics = []
  for n in range(len(dsm_fill)):
    if normalization:
      pics.append(np.stack((normalizeRela(dsm_fill[n]), normalizeRela(slope[n]), normalizeRela(layer[n])), axis=2))
  arr_pics = np.stack(pics)
  arr_pics = arr_pics.astype(np.float32)
  return arr_pics

