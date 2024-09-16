import os
from pathlib import Path
import pandas as pd
from projeto_vendas.projeto_venda_recuperando_arquivos import script_path

scirpt_path = os.getcwd()
def get_all_files_path():
    files_path = []
    # os.chdir(os.getcwd())
    path = Path(script_path + "/Vendas")

    # /Vendas
    for dir in path.iterdir():
        if dir.is_dir():
            # print(dir)
            os.chdir(dir)
            path = Path.cwd()
            # print(path)

            # Meses
            # 01 - Janeiro
            # 02 - Fevereiro
            # 03 - Março
            for dir in path.iterdir():
                if dir.is_dir():
                    os.chdir(dir)
                    path = Path.cwd()
                    # print(path)

                    # Arquivos
                    for file in path.iterdir():
                        if '.DS_Store' in file.name:
                            continue

                        files_path.append(file)

    return files_path

def get_vendas_loja(sales_df):
    total_sales = sales_df.groupby(by='Loja').sum()
    del(total_sales['Vendedor'])
    # print(total_sales)
    return total_sales


def get_sales_dataframe(files_path):
    sales_list = []

    for path in files_path:
        sale = pd.read_excel(path)
        sales_list.append(sale)  # Adiciona cada DataFrame à lista

    sales = pd.concat(sales_list, ignore_index=True)

    return sales

def get_vendas_vendedor(sales_df):
    total_sales = sales_df.groupby(by='Vendedor').sum()
    del(total_sales['Loja'])
    # print(total_sales)
    return total_sales

files_path = get_all_files_path()
sales_df = get_sales_dataframe(files_path)
vendas_loja = get_vendas_loja(sales_df)
vendas_vendedor = get_vendas_vendedor(sales_df)
# print(vendas_loja)
# print(vendas_vendedor)

os.chdir(script_path)
vendas_loja.to_excel('vendas_loja.xlsx')
vendas_vendedor.to_excel('vendas_vendedor.xlsx')

