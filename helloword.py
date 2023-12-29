email = "teste@email.com.br"
print(email)
posicao = email.find("@")
print("servidor", email[posicao+1:])
