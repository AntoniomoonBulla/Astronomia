import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import scipy


def convertir_formato_df(archivo):
    columnas = pd.read_csv(archivo, sep=" ", header=None)
    
    return columnas

archivo = open(r"thorio.dat")

tabla = convertir_formato_df(archivo)


def organizar_datos(tabla):
    pixel = np.array(tabla[0])
    intensidad = np.array(tabla[1])
    return pixel, intensidad

def graficar_datos(pixel, intensidad):
    plt.plot(pixel, intensidad)
    plt.title("Espectro del Torio")
    plt.xlabel("Pixel")
    plt.ylabel("Intensidad")
    plt.show()

pixel, intensidad = organizar_datos(tabla)
intensidad_normalizada = (intensidad - np.min(intensidad)) / (np.max(intensidad) - np.min(intensidad))

graficar_datos(pixel, intensidad_normalizada)

picos = scipy.signal.find_peaks(intensidad_normalizada, prominence=0.1, distance=20)
print("Los picos se encuentran en los siguientes pixeles: ", pixel[picos[0]])

distancia_entre_picos = np.diff(pixel[picos[0]])
print("La distancia entre los picos es: ", distancia_entre_picos)