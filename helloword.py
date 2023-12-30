email = "teste@email.com.br"
print(email)
posicao = email.find("@")
print("email", email[:posicao])
print("servidor", email[posicao+1:])