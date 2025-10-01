import numpy as np
ANNOTATION_TYPE_LIST = ['object_detection', 'instance_segmentation', 'classification', 'semantic_segmentation']

CROP_LIST = ["barley", "maize", "pearl_millet", "finger_millet", "rice", "sorghum", "wheat", "bush_bean",
             "climbing_bean", "chickpea", 'cowpea', "faba_bean", "grass_pea", "ground_nut", "lentil", "pigeonpea",
             "soybean", "banana", "cassava", "potato", "sweet_potato", "yam", "taro", "corn", "sugarcane"]

YEAR_LIST = np.arange(1900, 2050, 1)

TIME_OF_YEAR_LIST = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'fall', 'winter', 'spring',
                     'summer', 'short_rains', 'long_rains']

SOIL_COLOR = ["light", "dark", "red"]