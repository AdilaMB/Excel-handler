import pandas as pd
import io

# Load de file
my_file= pd.read_excel("C:\\Users\\Quiow\\Documents\\UEP-Digital\\301010 - Medidas Abertas.xlsx")

data = pd.DataFrame(my_file)

print (data.drop(data.index[0:1]))
print (data.drop(data.head))

#Save in csv
my_file.to_csv("C:\\Users\\Quiow\\Desktop\\csv\\datos.csv", sep=",", encoding="\n")
