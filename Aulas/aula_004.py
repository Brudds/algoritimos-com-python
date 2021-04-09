""""
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

resultado = valor1 + valor2
print(f'O resultado da soma é {resultado}')
print(f'O resultado da subtração é {valor1 - valor2}')
print(f'O resultado da multiplicação é {valor1 * valor2}')
print(f'O resultado da divisão é {valor1 / valor2}')
# Posso forçar o resultado ser int colocando {int(valor1 / valor2)}
"""
# Ordem de precedência

materia = input('Digite o nome da matéria: ')
nota1 = float(input(f'Digite sua primeira nota: '))
nota2 = float(input(f'Digite sua segunda nota: '))
nota3 = float(input(f'Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

print(f'Sua média em {materia} é {media:.2}')
# Posso formatar o numero de dígitos que aparecem usando ": .n°"
