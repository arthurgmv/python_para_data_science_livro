import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

Base_Dados = pd.read_csv('Startups+in+2021+end.csv')
Base_Dados.shape
print(Base_Dados.head())
print(Base_Dados.columns)