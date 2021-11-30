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

# Punto 2
municipios = len(data.groupby('Nombre municipio').size())
print(f'EL numero de municipios afectado es: {municipios}')

# Punto 3
municipios_afectados = data.groupby('Nombre municipio').size().sort_values(ascending=False)
print(f'\nMunicipios afectados: {municipios_afectados}')

# Punto 4
data['Ubicación del caso'].replace('Casa', 'CASA', inplace=True)
data['Ubicación del caso'].replace('casa', 'CASA', inplace=True) 
atencion_en_casa = len(data[data['Ubicación del caso'] == 'CASA'])
print(f'El numero de personas que se encuentran en atención en casa: {atencion_en_casa}')

# Punto 5
personas_recuperadas = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'El total de  personas recuperada es: {personas_recuperadas}') 

# Punto 6
personas_fallecidas = data[data['Estado'] == 'Fallecido'].shape[0]
print(f'El total de personas fallecidas en Colombia es de: {personas_fallecidas}')
