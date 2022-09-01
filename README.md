# Correcting global elevation models for canopy and infrastructure using Convolutional Neural Networks
## Introduction
A Digital Elevation Model (DEM) is a digital representation of the surface morphology and contains a wealth of topographic and geomorphological information necessary for analyzing geological applications. It has become one of the most important and basic geographic information data, and there is an increasing abundance of publicly released local and global DEM datasets. [polidori_digital_2020]

Accurate elevation data in DEMs are essential for many geoscience applications and other fields, such as soil erosion, reservoir planning, and flooding prediction. Notice that DEM is a generic term that concludes two surfaces model, the digital terrain model (DTM) and the digital surface model (DSM). Since it is widespread to use photogrammetry and LiDAR to produce DEMs, at the global scale, most DEMs are more like DSMs rather than DTMs. [polidori_digital_2020, hawker_30_2022]

Directly using DSMs in some applications will cause errors; for example, the threats might be underestimated in flooding prediction when using DSMs in urban or forested areas. [kulp_global_2016] Therefore, post-processing strategies must be used to remove height bias from trees and buildings so that the DEM can theoretically be considered a DTM.

Although this issue has been researched in some studies like [FABDEM, CoastalDEM], which convert global DSMs to DTMs, there are some drawbacks in their methods: 1) Besides DSM pixels, they need extra inputs from other sources like population density and vegetation density; 2) There are artifacts created in the results. Some deep learning methods that are successful in computer vision have been used in DTM extracting recently; however, most studies rely on multiple bands of imagery or point clouds as inputs. [meadowsComparisonMachineLearning2021, kazimiDETECTIONTERRAINSTRUCTURES2020, gevaertDeepLearningApproach2018]

This project uses a fully convolutional network (FCN) for semantic segmentation and aims to:
1. Use only DSM as input;
2. Apply this model on DSMs with higher resolution.
The project will benefit applications that need the correct terrain representation and further research on correcting DEMs with machine learning.
