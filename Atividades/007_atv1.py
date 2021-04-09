import datetime

anoAtual = datetime.date.today().year
anoNascimento = int(input("Digite aqui o ano que você nasceu: "))

print(f"Certo, então você tem {anoAtual - anoNascimento} anos.")
