
import numpy as np;

l1 = np.array([1,2,3]);
l2 = np.array([[4,5,6], [1,2,3], [3,7,8]]);
print(l1+l2);
print(l1*l2);
print(np.sum(l2)); #suma
print(np.product(l1)); #multiplicación

print(np.random.rand(10)); # generar numeros aleatorios



a = np.random.randint(1, 20) # generar numeros enteros en un rango determinado
print(a);

a = np.arange(15).reshape(3,5); # crear arreglos con un rango determinado
print(a);

print(" ");

b = np.random.randint(1,16, size=(3,5));
print(b);

b = np.random.randint(1,16, size=(3,5));
print(b);

print(np.max(b));

li = np.arange(20); # CREAR ARREGLO
print(li[li%2==0]);

print(np.argmax(li));
print(np.argmin(li));

l2 = np.arange(1,21,2); # CREAR ARREGLO CON UN RANGO DETERMINADO
print(l2);

a = np.zeros((3,4));
print(a);

print(" ");

b = np.ones((3,4));
print(b);

a = np.eye(4);
print(a);

print(" ");

b = np.identity(4);
print(b);