# -*- coding: utf-8 -*-
"""Taller2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MShfnsujzqNwcVS6gzpdVaG8z5B5Z_pQ
"""

import numpy as np;

# 1. Crear un array con los numeros impares entre 20 y 70
numerosImpares = np.arange(10, 50);
print(numerosImpares[numerosImpares % 2 != 0]);

# 2. Crear un array de 20 elementos, con numeros aleatorios entre 10 y 50 filtrar los numeros mayores a 35
array = np.random.randint(10, 51, size=20);
numerosMayores = array[np.where(array > 35)]
print(numerosMayores);

# 3. Filtrar los animales cuya longitud de caracteres es menor a 4, en el array:
animales = np.array(["perro", "gato", "leon", "tigre", "ave", "zancudo", "oso", "jirafa", "elefante"]);

caracteresMenora4 = animales[np.where(np.char.str_len(animales) < 4)];
print(caracteresMenora4);

# 4. Crea una matriz de 4x4 con valores aleatorios entre 1 y 9, filtrar las columnas donde la suma sea mayor a 12
matriz = np.random.randint(1,10, size=(4,4));
print(matriz);

print("************")

sumaColumnas = np.sum(matriz, axis=0);

columnasMayora12 = matriz[:, sumaColumnas > 12];

print(columnasMayora12);

# 5. En el array del punto 2, filtrar los valores de las posiciones 2, 4, 6, 9, 11

array = np.random.randint(10, 51, size=20);
print(array);

print("************");

posiciones = [2, 4, 6, 9, 11];

valores = array[posiciones];

print(valores);

# 6. Completar el array con 10 datos más y filtrar luego por los de genero femenino

array = np.array([
    ["Roberto", "casado", "masculino"],
    ["Sheila", "soltero", "femenino"],
    ["Bruno", "soltero", "masculino"],
    ["Rita", "casado", "femenino"],
    ["Pedro", "casado", "masculino"],
    ["Laura", "soltero", "femenino"],
    ["Juan", "casado", "masculino"],
    ["María", "soltero", "femenino"],
    ["Carlos", "casado", "masculino"],
    ["Sofía", "soltero", "femenino"],
    ["Miguel", "casado", "masculino"],
    ["Ana", "casado", "femenino"],
    ["Diego", "soltero", "masculino"],
    ["Elena", "casado", "femenino"]
]);

generoFemenino = array[array[:, 2] == "femenino"];

print(generoFemenino);