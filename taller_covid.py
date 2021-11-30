# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:30:50 2021

@author: USER
"""

import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# Punto 1
numero_de_casos = data.shape[0]
print(f'El numero de casos de contagios en el pais es de: {numero_de_casos}')

