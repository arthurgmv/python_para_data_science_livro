#Lendo um arquivo de planilha
import pandas as pd
titanic = pd.io.parsers.read_csv('titanic.csv')
x = titanic[['Age']]
print(x)