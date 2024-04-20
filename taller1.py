import numpy as np;

## 1. Crear arreglo de 10 ceros

arreglo = np.zeros(10);
print(arreglo);

# 2. Crear arreglo con 10 unos

arreglo2 = np.ones(10);
print(arreglo2);

# 3. Crear arreglo de 10 cincos

arreglo3 = np.ones(10) * 7;
print(arreglo3)

# 4. Crear arreglo con numeros enteros del 10 al 50;

numerosEnteros = np.arange(10, 50);
print(numerosEnteros);

# 5. Crear un arreglo con todos los numeros pares del 10 al 50
numerosEnteros = np.arange(10, 50);
print(numerosEnteros[numerosEnteros % 2 == 0]);

# 6. Crear una matriz de 3x3 con valores del 0 al 1
matriz = np.random.randint(0,9, size=(3,3));
print(matriz);

# 7. Crear una matriz de identidad(con 1 en la diagonal) de 3x3
m = np.eye(3);
print(m);

#8. Generar un número aleatorio entre 0 y 1
print(np.random.random());