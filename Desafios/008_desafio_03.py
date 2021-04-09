property = float(input("Informe o valor do imóvel a ser adquirido: "))
monthlyIncome = float(input("Informe seu salário: "))
years = int(input("Em quantos anos deseja pagar: "))

months = (years * 12)
installments = (property / months)
incomeLimit = (monthlyIncome * 0.3)

print(f"A prestação do imóvel será de R${installments}")
print(f"O limite permitido da sua renda é de R${incomeLimit}")

if installments <= incomeLimit:
    print("Seu empréstimo foi aprovado.")
else:
    print("Seu empréstimo foi negado.")
