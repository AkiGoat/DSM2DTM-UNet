from qgis.core import *
import qgis.utils

import processing

processing.run(
    "saga:resampling", {
        'INPUT': '/Volumes/HydesT7/Grad Project/Data/ANH4_all/R5_67HZ1.TIF',
        'KEEP_TYPE': True,
        'SCALE_UP': 5,
        'SCALE_DOWN': 3,
        'TARGET_USER_XMIN TARGET_USER_XMAX TARGET_USER_YMIN TARGET_USER_YMAX':
        None,
        'TARGET_USER_SIZE': 30,
        'TARGET_USER_FITS': 1,
        'TARGET_TEMPLATE': None,
        'OUTPUT':
        '/Volumes/HydesT7/Grad Project/Data/ANH4_QGIS/R5_67HZ1_30.sdat'
    })
