nomes = ['Bruno', 'Saymon', 'Augusto', 'Caio', 'Joao']
mensagens = []

for i in range(5):
    msg = input("Adicione uma mensagem para seu amigo " + nomes[i] + ": ")
    mensagens.append(msg)

print("Os nomes ficaram desta forma:", nomes[0], mensagens[0], ",", nomes[1], mensagens[1], ",", nomes[2], mensagens[2], ",", nomes[3], mensagens[3], ",", nomes[4], mensagens[4])
