import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import scipy
import os


ruta = os.path.join(os.path.dirname(__file__), "thar.ascii")

def convertir_formato_df(archivo):
    return pd.read_csv(archivo, sep=r"\s+", header=None)

tabla = convertir_formato_df(ruta)
wavelength = tabla[0]
intensidad = tabla[1]

wavelength = np.array(wavelength)
intensidad = np.array(intensidad)

wavelength_grafico = []
intensidad_grafico = []

for i in range(len(wavelength)):
    if 5845 <= wavelength[i] <= 5930:
        wavelength_grafico.append(wavelength[i])

for i in range(len(intensidad)):
    if 5845 <= wavelength[i] <= 5930:
        intensidad_grafico.append(intensidad[i])


grafico = plt.figure(figsize=(14, 5))
plt.plot(wavelength_grafico, intensidad_grafico, color="red")
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.title("Spectral lines of the Sun")
plt.tight_layout()
plt.show()

picos = scipy.signal.find_peaks(intensidad_grafico, distance=40)

pixel = [wavelength_grafico[i] for i in picos[0]]

diferencias = np.diff(pixel)

print("La distancia entre los picos es: ", diferencias)
