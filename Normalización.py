import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import scipy


def convertir_formato_df(archivo):
    columnas = pd.read_csv(archivo, sep=" ", header=None)
    
    return columnas

archivo = open(r"espectro sol.dat")

tabla = convertir_formato_df(archivo)


def organizar_datos(tabla):
    pixel = np.array(tabla[0])
    intensidad = np.array(tabla[1])
    return pixel, intensidad

def graficar_datos(pixel, intensidad):
    plt.plot(pixel, intensidad)
    plt.title("Espectro del Sol")
    plt.xlabel("Pixel")
    plt.ylabel("Intensidad")
    plt.grid()
    plt.show()

pixel, intensidad = organizar_datos(tabla)




picos = scipy.signal.find_peaks(intensidad, distance=40)

x_max = pixel[picos[0]]
y_max = intensidad[picos[0]]

print("Los picos se encuentran en los siguientes pixeles: ", x_max)
print("Los picos se encuentran en las siguientes intensidades: ", y_max)

ajuste = np.polyfit(x_max, y_max, 4)
polinomio = np.poly1d(ajuste)
continuo = polinomio(pixel)
grafico_ajuste = np.polyval(ajuste, x_max)

plt.figure(figsize=(14, 5))
plt.plot(pixel, intensidad, label="Picos", color="red")
plt.plot(x_max, grafico_ajuste, label="Ajuste polinomial", color="lime")
plt.title("Ajuste polinomial a los picos del espectro del Sol")
plt.xlabel("Pixel")
plt.ylabel("Intensidad")
plt.legend()
plt.grid(False)
plt.tight_layout()
plt.savefig("Ajuste polinomial a los picos del espectro del Sol.png", dpi=300)
plt.close()

#Normalización de los datos

def normalizar_datos(intensidad, continuo):
    intensidad_normalizada = intensidad/continuo
    plt.figure(figsize=(14, 5))
    plt.plot(pixel, intensidad_normalizada, color="black")
    plt.title("Normalización de los datos del espectro del Sol" , color="black")
    plt.xlabel("Pixel")
    plt.ylabel("Intensidad normalizada")
    plt.grid(False)
    plt.tight_layout()
    plt.savefig("Normalización de los datos del espectro del Sol.png", dpi=300)
    return intensidad_normalizada

intensidad_normalizada = normalizar_datos(intensidad, continuo)






