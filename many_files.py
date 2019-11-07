import sys
import csv
import glob
import pandas as pd

# get data file names
path =r'C:\Users\Adila\Desktop\csv'
filenames = glob.glob(path + "/*.xlsx")

for f in filenames:
    file = f
    my_file= pd.read_excel(f)
    data = pd.DataFrame(my_file)





    # Another way
    # Delete column
    # data = data.drop([0,1], axis=0)
    # data = data.iloc[2:,]

    # count column
    # data.columns = range(data.shape[1])

    # Get the column
    # data.columns = data.loc[1]