import pandas as pd
import pandasql as psql

def pysqldf(q):
    return psql.sqldf(q, globals())

df_pessoas = pd.read_excel('Pessoas.xlsx')

result = pysqldf(
    '''
    SELECT Nome, Idade FROM df_pessoas
    WHERE Idade > 85
    ORDER BY Idade ASC
    '''
)

print(result)
