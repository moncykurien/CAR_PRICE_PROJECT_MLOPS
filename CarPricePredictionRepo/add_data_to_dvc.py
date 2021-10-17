import os
from glob import glob

data_dir = ["data_extracts"]

for dir in data_dir:
    files = glob(dir+r'/*.csv')
    for file_ in files:
        os.system(f"dvc add {file_}")
print("\n####All files added to dvc.####")