import pandas as pd

#DataFrame com List
data = [10, 20, 30]

df01 = pd.DataFrame(data)
#print(df01)

#DataFrame com matriz
dados = [
    ["Alex", 10],
    ["Bart", 12],
    ["Caio", 13]
]
df02 = pd.DataFrame(dados, columns=["Nome", "Idade"])
#print(df02)

#DataFrame com Dicionário
dados02 = {
    'Nome': ['Tomé', 'João', 'Paulo', 'Pedro'],
    'Idade': [28, 34, 29, 42]
}
df03 = pd.DataFrame(dados02)
print(df03)