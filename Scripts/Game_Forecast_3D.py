import pandas as pd
file_dir=r"./work_02.csv"
file=pd.read_csv(file_dir,header=None,encoding= 'utf-8')
index=len(file)