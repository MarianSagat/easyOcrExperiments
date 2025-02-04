import os
from unit_test import UnitTest

# %% Set up paths 
easyocr_module = "D:/Documents/documents 2024/neural networks/code/EasyOCR2/easyocr"
verbose = 2
test_data = "D:/Documents/documents 2024/neural networks/code/EasyOCR2/unit_test/data/EasyOcrUnitTestPackage.pickle"
image_data_dir = "D:/Documents/documents 2024/neural networks/code/EasyOCR2/examples"

# %% Initialize UnitTest
unit_test = UnitTest(easyocr_module, 
                     test_data,
                     image_data_dir
                     )
# %% Run UnitTest at verbosity level 2
unit_test.do_test(verbose = 2)