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

#I take the 3rd line and put it in the title of each column
    cabezal = data.iloc[1]
    data.columns = cabezal

#Name of the file and path
    new_nome = "dato.csv"
    path = r'C:\\Users\\Adila\\Desktop\\csv\\'

    # Save in csv
    data.to_csv(path + new_nome, sep=";", encoding="utf8")


    # -------------------------Another way--------------------------
    # Delete column
    # data = data.drop([0,1], axis=0)
    # data = data.iloc[2:,]

    # count column
    # data.columns = range(data.shape[1])

    # -------------- Get the column
    # data.columns = data.loc[1]

    #--------------- Load de file
    # file = r"C:\\Users\\Adila\\Desktop\\csv\\301010 - Medidas Encerradas.xlsx"
    # my_file= pd.read_excel(file)
    # data = pd.DataFrame(my_file)