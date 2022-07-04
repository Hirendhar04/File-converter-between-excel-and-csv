import pandas as pd
import os
import glob

current_folder = os.getcwd()
print(current_folder)

csv_list = glob.glob(os.path.join("*.csv"))
print(csv_list)

converted_file_prefix = 'file'
index = 0
for file in csv_list:
    df = pd.read_csv(file)
    df.to_excel(converted_file_prefix+str(index)+ ".xlsx")
    index = index = 1