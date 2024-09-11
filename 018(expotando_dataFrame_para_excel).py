import pandas as pd

data = {
    'UNIDADES': pd.Series([1, 2, 3]),
    'DEZENAS': pd.Series([11, 20, 30])
}
df = pd.DataFrame(data)

workbook = 'Numeros_DataFrame.xlsx'
sheet = 'Aba1'

df.to_excel(workbook, sheet_name=sheet, index=False)
