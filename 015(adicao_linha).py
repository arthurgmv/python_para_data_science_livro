import pandas as pd

columns = ['UNIDADES', 'DEZENAS']
rows = [
    [1,10],
    [2, 20]
]

df = pd.DataFrame(rows, columns=columns)
print(df)
print('-------------------------')

row2 = [
    [3,30]
]

df2 = pd.DataFrame(row2, columns=columns)

df = df._append(df2, ignore_index=True)
print(df)
print('-------------------------')