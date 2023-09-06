import glob
import os

relative_path = "0_python/*01*"

file_paths = glob.glob(relative_path)
files = [os.path.basename(file) for file in file_paths]
print(files)
