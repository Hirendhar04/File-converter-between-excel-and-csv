import pandas as pd
import os
import glob


current_folder = os.getcwd()
print(current_folder)

excel_list = glob.glob(os.path.join("*.xlsx"))
print(excel_list)

converted_file_prefix = 'file'
index = 0
for file in excel_list:
    df = pd.read_excel(file)
    df.to_csv(converted_file_prefix+str(index)+ ".csv")
    index = index = 1
 
    
