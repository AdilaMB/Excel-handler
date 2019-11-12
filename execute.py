import glob
import pandas as pd

#-----Handle of file------------
# Get data file names
path = r'C:\\Users\\Adila\\Desktop\\csv\\'
filenames = glob.glob(path + "/*.xlsx")
#New file for save all head
new_dataFrame = pd.DataFrame()
writer = 'C:\\Users\\Adila\\Desktop\\csv\\datos.xlsx'

for f in filenames:
    file = f
    my_file = pd.read_excel(f)
    data = pd.DataFrame(my_file)

#-----Work with to copy head for new excel----------
    #I take the 3rd line and put it in the title of each column
    cabezal = data.iloc[1]
    data.columns = cabezal
    # Creo nuevo DataFrame com el cabezal y lo concateno en el fichero datos.xlsx
    df = pd.DataFrame([cabezal], columns=[cabezal])
    df.iloc[:0] = file
    # Concat both DataFrames
    new_dataFrame = new_dataFrame.append(df)
    # Save auxiliary excel
    new_dataFrame.to_excel(writer, 'Cabecalhos', index=False)

#------Delete the first 2 rows
    data = data.drop([0, 1], axis=0)

#------Work to add 2 columns with fragmented file name---------
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

#-------Save in csv format----------------------------------
    new_nome = str(platform + "-" + status + ".csv")
    data.to_csv(path + new_nome, sep=";", encoding="utf8")