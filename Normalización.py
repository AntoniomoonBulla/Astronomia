import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def convertir_formato_csv(archivo):
    columnas = pd.read_csv(archivo, delimiter=" ")
    
    return pd.DataFrame(columnas)

archivo = open(r"C:\Users\Antonio\Documents\Astro - Visual Code\Astronomia\espectro sol.dat")

tabla = convertir_formato_csv(archivo)


def organizar_datos():
    pd.read_csv
