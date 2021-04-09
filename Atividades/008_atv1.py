import random
from time import sleep

numeroSorteado = random.randint(0, 5)
numeroEscolhido = int(input("Digite aqui um numero de 0 a 5 : "))

print("Hmm... deixe-me ver...")
sleep(3)
if numeroSorteado == numeroEscolhido:
    print("Parabéns, você ganhou!!")
else:
    print(f"Vish, não foi dessa vez. O número sorteado foi {numeroSorteado}")
    print("Mais sorte na próxima.")
