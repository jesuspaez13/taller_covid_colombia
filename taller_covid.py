# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:30:50 2021

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Punto 7
tipo_de_caso_importado = data.groupby('Tipo de contagio').size().sort_values(ascending=False)
print(f'{tipo_de_caso_importado}')

# Punto 8
departamentos_afectados = len(data.groupby('Nombre departamento').size())
print(f'EL numero de municipios afectado es de: {departamentos_afectados}')

# Punto 9
data.groupby('Nombre departamento').size()

# Punto 10
tipo_de_atencion = data.groupby('Ubicación del caso').size().sort_values(ascending=False)
print(f'{tipo_de_atencion}')

# Punto 11
orden_departamento= data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'Los 10 departamentos con mas casos de contagiados son: {orden_departamento}')

# Punto 12
depar_falle = data[data['Estado'] == 'Fallecido'].groupby(
 'Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'\n{depar_falle}')

# Punto 13
depar_recup = data[data['Recuperado'] == 'Recuperado'].groupby(
 'Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'\n{depar_recup}')

# Punto 14
mas_contagiados = data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print(f' {mas_contagiados}')

# Punto 15
muni_falle = data[data['Estado'] == 'Fallecido'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'\n{muni_falle}')

# Punto 16
muni_recup = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'\n{muni_recup}')

# Punto 17
dpto_ciudades = data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values(ascending=False)
print(f'{dpto_ciudades}')

# Punto 18
numero_personas = data.groupby(['Nombre departamento', 'Nombre municipio','Sexo']).size().sort_values(ascending=False)
print(f' {numero_personas}')

# Punto 19
promedio = data.groupby( ['Nombre departamento', 'Nombre municipio', 'Sexo']).Edad.mean()
print(f'{promedio}')

# Punto 20
procedencia = data['Nombre del país'].value_counts()
print(f'{procedencia}')

# Punto 21
fech_contagio = data.groupby(
    ['Fecha de diagnóstico']).size().sort_values(ascending=False)
print(f'\n{fech_contagio}')

# Punto 22
mortalidad = (len(data[data['Estado'] == 'Fallecido']) / len(data)) * 100
recuperacion = (len(data[data['Recuperado'] == 'Recuperado']) / len(data)) * 100
print('\nTasa de mortalidad: ', "{:.2f}".format(mortalidad))
print('\nTasa de recuperacion: ', "{:.2f}".format(recuperacion))

# Punto 23
tasa_mortalidad = (data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size() / len(data)) * 100
print(f' tasa de mortalidad por Departamento: {tasa_mortalidad}')
tasa_recuperacion = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size() / len(data)) * 100
print(f'r tasa de recuperación por departamento: {tasa_recuperacion}')

# Punto 24
muerte_ciudad = (data[data['Recuperado'] == 'fallecido'].groupby('Nombre municipio').size() / len(data)) * 100
print(f'tasa de mortalidad  por ciudad es: {muerte_ciudad}')
recuperacion_ciudad = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size() / len(data)) * 100
print(f'L tasa de recuperación por municipio es: {recuperacion_ciudad}')

# Punto 25
atencion = data.groupby(['Nombre municipio', 'Ubicación del caso']).size()
print(f'\n{atencion}')

# Punto 26
prom_edad_sexo = data.groupby(['Nombre municipio', 'Sexo']).Edad.mean()
print(f'\n{prom_edad_sexo}')

# Punto 27
data['Sexo'].replace('f', 'F', inplace=True)
data['Sexo'].replace('m', 'M', inplace=True)
data['Estado'].replace('LEVE', 'Leve', inplace=True)
data['Estado'].replace('leve', 'Leve', inplace=True)

contg = data.groupby('Fecha de diagnóstico').size(
).sort_values().plot(figsize=(15, 4))
print('\nCurva de Contagios')
plt.show(contg)

falle = data[data['Recuperado'] == 'fallecido'].groupby(
    'Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Fallecidos')
plt.show(falle)

recup = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Recuperados')
plt.show(recup)

# Punto 28
curv_contg_depar = data.groupby('Nombre departamento').size(
).sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas contagios')
plt.show(curv_contg_depar)

curv_falle_depar = data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas personas fallecidas')
plt.show(curv_falle_depar)

curv_recu_depar = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas personas recuperadas')
plt.show(curv_recu_depar)

# Punto 29
curv_contg_munic = data.groupby('Nombre municipio').size(
).sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas contagios')
plt.show(curv_contg_munic)

curv_falle_munic = data[data['Recuperado'] == 'fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas personas fallecidas')
plt.show(curv_falle_munic)

curv_recu_munic = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas personas recuperadas')
plt.show(curv_recu_munic)

# Punto 30
fallecidos = data[data['Recuperado'] == 'fallecido'].groupby('Edad').size().sort_values(ascending = False)
print(f'{fallecidos}')
