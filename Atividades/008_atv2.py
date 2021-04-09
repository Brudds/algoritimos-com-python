# Simulando radar com limite máximo de 80km/h
from random import randrange

velocidadeCarro = randrange(60, 120, 10)

if velocidadeCarro > 80:
    print(f"O carro estava a {velocidadeCarro}km/h, excedendo o limite de 80km/h.")
    print(f"Você foi multado em R${(velocidadeCarro - 80) * 7}.")
else:
    print(f"O carro estava a {velocidadeCarro}km/h respeitando o limite de 80km/h.")
    print("Pode seguir viagem.")
