# Módulos

""""

Posso importar algumas funções ao invés de todas
como por exemplo
from math import ceil, floor, factorial
assim, posso utilizar como: print(f"Arredondado pra cima: {ceil(numero)}")

"""
import math

numero = float(input("Digite um número quebrado: "))
print(f"Arredondado pra cima: {math.ceil(numero)}")
print(f"Arredondado pra baixo: {math.floor(numero)}")
print(f"Factorial: {math.factorial(int(numero))}")
