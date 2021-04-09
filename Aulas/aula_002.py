nome = input("Digite o seu primeiro nome: ")
sobrenome = input("Agora, digite seu sobrenome: ")

# 1° forma de contatenar -> junto tudo com + e printa depois
# 2° forma de contatenar -> printa formatando o texto print(f"aaaa {variavel} aaaa")
# 3° forma de contatenar -> coloca o texto e formata o espaço print("aaa {} aaa".format(variavel,variavel))
# anotações maneira do professor com exemplo de pedido:

# Primeira forma de concatenar texto.
# pedidoCliente = "Beleza. Vamos preparar para comer " + comida + ". E para beber, no capricho vai " + bebida + ". Aguarde seu pedido!"

# Segunda forma de concatenar texto.
# print(f"Vamos preparar para comer {comida}. E para beber no capricho {bebida}. Aguarde seu pedido!")

# Terceira forma de concatenar texto.
#print("Vamos preparar para comer {}. E para beber no capricho {}. Aguarde seu pedido".format(comida, bebida))

nomeCompleto1 = nome + " " + sobrenome

print(f'Certo, seu nome é: {nomeCompleto1}.')




