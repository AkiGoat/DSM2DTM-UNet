import os
import PIL
import torch
import numpy as np
import pandas as pd
from torch.utils.data import Dataset


class SurrData(Dataset):
    def __init__(self, setname):
        """
        Variables:
       <setname> can be any of: 'train' to specify the training set
                                'test' to specify the test set"""
        self.setname = setname
        assert setname in ['train', 'val', 'test']

        # Define dataset
        overall_dataset_dir = '/Volumes/SamDick/Grad Project/Data/ML'
        self.selected_dataset_dir = os.path.join(overall_dataset_dir, setname)

        # E.g. self.all_filenames = ['006.png','007.png','008.png'] when setname=='val'
        self.all_filenames = os.listdir(self.selected_dataset_dir)
        self.all_labels = pd.read_csv(os.path.join(overall_dataset_dir, 'labels.csv'), header=0, index_col=0)
        self.label_meanings = self.all_labels.columns.values.tolist()

    def __len__(self):
        """Return the total number of examples in this split, e.g. if
        self.setname=='train' then return the total number of examples
        in the training set"""
        return len(self.all_filenames)

    def __getitem__(self, idx):
        """Return the example at index [idx]. The example is a dict with keys
        'data' (value: Tensor for an RGB image) and 'label' (value: multi-hot
        vector as Torch tensor of gr truth class labels)."""
        selected_filename = self.all_filenames[idx]
        #         imagepil = PIL.Image.open(os.path.join(self.selected_dataset_dir,selected_filename)).convert('RGB')

        #         #convert image to Tensor and normalize
        #         image = utils.to_tensor_and_normalize(imagepil)

        npy = np.load(os.path.join(self.selected_dataset_dir, selected_filename))
        pimg = torch.from_numpy(npy).float()

        # load label
        label = torch.Tensor(self.all_labels.loc[selected_filename, :].values)

        sample = {'data': pimg,  # preprocessed image, for input into NN
                  'label': label,
                  'img_idx': idx}
        return sample