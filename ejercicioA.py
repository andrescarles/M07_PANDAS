import pandas as pd
import matplotlib.pyplot as plt

#IMPORTAMOS EL ARCHIVO : SI QUIERES USAR UNA MUESTRA DE 2 PAISES ESTA EL ARCHIVO data2.csv
df = pd.read_csv('data2.csv')#data2.csv

#EXTRAEMOS EL MES DE LA FECHA
df['month'] = pd.DatetimeIndex(df['date']).month


#REALMENTE PODRIA USARSE SOLO 1 FUNCION YA QUE TODAS SON IGUALES, NO SE ESPERABA ESTE RESULTADO.
def funcion1():
    array = []
    #df_resultado almacena el df agrupado por dos columnas, sum() suma los rows numericos.
    df_resultado = df.groupby(['location','month']).sum()
    #Este bucle corta el dataframe en grupos de 12 meses y los va añadiendo en un array.
    for i in range(0, df_resultado.shape[0], 12):
        array.append(df_resultado.iloc[i:i+12, :])
    #retornamos una lista con dataframes de 12 rows.
    return array

def funcion2():
    array = []
    df_resultado = df.groupby(['location','month']).sum()
    for i in range(0, df_resultado.shape[0], 12):
        array.append(df_resultado.iloc[i:i+12, :])
    return array

def funcion3():
    array = []
    df_resultado = df.groupby(['location','month']).sum()
    for i in range(0, df_resultado.shape[0], 12):
        array.append(df_resultado.iloc[i:i+12, :])
    return array


   
    
