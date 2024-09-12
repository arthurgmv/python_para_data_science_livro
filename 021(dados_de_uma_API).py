import requests
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/photos'

r = requests.get(url)
data = r.json()

df = pd.DataFrame(data)
print('Exportando para .xlsx')
df.to_excel('destino.xlsx', index=False)
print('Exportação finalizada com sucesso.')
