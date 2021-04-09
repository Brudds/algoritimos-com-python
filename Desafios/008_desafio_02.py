number1 = float(input("Escolha um primeiro número: "))
number2 = float(input("Agora escolha um segundo número: "))
number3 = float(input("Por fim, escolha um terceiro número: "))

if number1 > number2 and number1 > number3:
    print(f"O maior número escolhido foi o {number1}.")
if number2 > number1 and number2 > number3:
    print(f"O maior número escolhido foi o {number2}.")
if number3 > number2 and number3 > number1:
    print(f"O maior número escolhido foi o {number3}.")

if number1 < number2 and number1 < number3:
    print(f"O menor número escolhido foi o {number1}.")
if number2 < number1 and number2 < number3:
    print(f"O menor número escolhido foi o {number2}.")
if number3 < number2 and number3 < number1:
    print(f"O menor número escolhido foi o {number3}.")
