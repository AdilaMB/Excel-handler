import sys
import csv
import glob
import pandas as pd

# get data file names
path = r'C:\\Users\\Adila\\Desktop\\csv\\'
filenames = glob.glob(path + "/*.xlsx")

for f in filenames:
    file = f
    my_file = pd.read_excel(f)
    data = pd.DataFrame(my_file)

    #I take the 3rd line and put it in the title of each column
    cabezal = data.iloc[1]
    data.columns = cabezal

    # Delete de white rows
    data = data.drop([0, 1], axis=0)

    # Calculate the last column and insert new column
    new_column_platform = 0
    new_column_status = 0
    last_column = data.shape[1]
    new_column_platform += last_column
    new_column_status += new_column_platform
    last_row = data.shape[0]

    # Work with string for insert the last column
    text = file.split('-')
    aux_status = text[len(text) - 1].split('.')
    aux_platform = text[len(text) - 2].split('\\')
    status = aux_status[0]

    platform = aux_platform[len(aux_platform) - 1]

    # Add values in the new columns
    for row in range(1, last_row):
        data['Platform'] = platform
        data['Status_Medida'] = status

    # Name of the new file, converted into csv extension
    new_nome = str(platform + "-" + status + ".csv")
    # new_path = r'C:\\Users\\Adila\\Desktop\\csv\\'

    # Save in csv
    data.to_csv(path + new_nome, sep=";", encoding="utf8")