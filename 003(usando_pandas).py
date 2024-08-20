#Usando a biblioteca pandas para ler o arquivo como tabela
import pandas as pd
Colors_table = pd.io.parsers.read_table('Colors.txt')
print(Colors_table)

