from operator import index
import pandas as pd


df_unidades = pd.DataFrame({'UNIDADES': [1,2,3]})
df_dezenas = pd.DataFrame({'DEZENAS': [10,20,30]})

writer = pd.ExcelWriter('Numeros.xlsx')

df_unidades.to_excel(writer, sheet_name='Unidades', index=False)
df_dezenas.to_excel(writer, sheet_name='Dezenas', index=False)

writer.close()
