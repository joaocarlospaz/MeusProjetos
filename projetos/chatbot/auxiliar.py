# modelo de conversa

mensagem1 = {"role": "assitant", "content": "Bora aprender Python?"}
mensagem2 = {"role": "user", "content": "Bora aprender"}
mensagem3 = {"role": "assitant", "content": "Bora aprender Python"}

lista_de_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role": "assitant", "content": "Opa, agora bora aprender Python!"}
lista_de_mensagens.append(nova_mensagem)

print(lista_de_mensagens)