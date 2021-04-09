name =  input("Digite aqui o seu nome: ")
schoolSubject = input("Qual disciplina você deseja saber sua média? ")
grade1 = float(input("Informe sua Nota da Prova: "))
grade2 = float(input("Informe sua Nota do trabalho prático: "))
grade3 = float(input("Informe sua Nota do projeto final nota: "))
average = (grade1 + grade2 + grade3) / 3

print(f"Você obteve a média final de {average}.")
if average >= 7:
    print("Parabéns, você foi aprovado.")
else:
    print("Infelizmente você foi reprovado.")
