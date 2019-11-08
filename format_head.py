#!/usr/bin/env python
# coding: utf-8

# In[48]:


import openpyxl
from openpyxl import load_workbook
import pandas as pd
import glob
import io 



"""
Função para formatar texto de título
"""
def formataTextoTitulo(frase):
    stringFormatada = frase.translate({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\\|~-=+ "})
    #stringFormatada = (unicodedata.normalize('NFKD', stringFormatada).encode('ascii', 'ignore')).decode("utf-8")
    return stringFormatada

"""
para o arquivo de saída precisa melhorar a formatacao
uma coluna nao pode ter espaço
uma coluna nao pode começar com numeros ou char special
o final de uma linha não pode ser ;
a coluna nao pode ter charspecial
a coluna nao pode ter acentos etc
para todas as tabelas deve ser craido uma coluna extra META_REPCOL
originalmente o conteudo da coluna serve como um identificador da linha
essa coluna no primeiro momento irá ter o memso valor da priemira coluna da tabela, nao tem problema se for null
"""

def formataTituloColuna(texto):
    stringFormatada = ''
    stringtexto = ''
    if (texto[0][2].isdigit()):
        stringtexto = 'C' + str(idColuna)

    if (len(texto) > 1):
        frase = self.montaFrase(texto)
    else:
        frase = texto[0][2]

    stringtexto += self.formataTextoTitulo(frase)
    if (stringtexto.isdigit() or (len(stringtexto) < 1)):
        if (len(stringtexto) > 0):
            stringFormatada = 'C' + str(idColuna) + "_" + str(stringtexto)
        else:
            stringFormatada = 'C' + str(idColuna)
    else:
        stringFormatada = stringtexto

    stringFormatada = stringFormatada[:30]

    return stringFormatada


# Load de file
#file = r"C:\\Users\\Quiow\\Documents\\UEP-Digital\\301010 - Medidas Abertas.xlsx"

# get data file names
path = r'C:\\Users\\Quiow\\Documents\\UEP-Digital\\'
filenames = glob.glob(path + "/*.xlsx")

for f in filenames:
    file = f
    my_file = pd.read_excel(f)
    data = pd.DataFrame(my_file)

    #I take the 3rd line and put it in the title of each column
    cabezal_origin = data.iloc[1]
    print (cabezal_origin)
    cabezal_format = formataTextoTitulo(str(cabezal_origin))
    print (cabezal_format)
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
        data['Plataforma'] = platform
        data['Status Medida'] = status

    # Name of the new file, converted into csv extension
    new_nome = str(platform + "-" + status + ".csv")
    

    # Save in csv
    data.to_csv(path + new_nome, sep=",", encoding="utf8")





    


# In[64]:


import openpyxl
from openpyxl import load_workbook
import pandas as pd
import glob
import io
import numpy as np

"""
Função para formatar texto de título
"""
def formataTextoTitulo(frase):
    stringFormatada = frase.translate({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\\|~-=+"})
    #stringFormatada = (unicodedata.normalize('NFKD', stringFormatada).encode('ascii', 'ignore')).decode("utf-8")
    return stringFormatada

#--------------- Load de file
file = r"C:\Users\Quiow\Documents\UEP-Digital\301010 - Medidas Abertas.xlsx"
my_file= pd.read_excel(file)
data = pd.DataFrame(my_file)

#I take the 3rd line and put it in the title of each column
cabezal_origin = data.iloc[1].values
print (cabezal_origin)

#new DataFrame
df = pd.DataFrame(columns = [cabezal_origin])
#print (df)

for i in cabezal_origin:
    cabezal_format = formataTextoTitulo(str(cabezal_origin))
    print (cabezal_format)
    if i == "nan":
        i = "Vazio"
    novo = pd.DataFrame(columns = [columns.append[i]])
    
print (novo)

#np.save(cabezal_origin, "dato.csv")

#cabezal_origin.save(path + new_nome, sep=",", encoding="utf8")


# In[ ]:





# In[ ]:




