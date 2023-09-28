""" Desenvolva um script em linguagem Python, utilizando Dicionários, que
solicite ao usuário inserir o nome de três produtos de mercado e seus
respectivos preços e os mostre na tela. """

d = {}


for i in range (1,4):
    prod = str(input("Insira o nome do produto numero: " + str(i)))
    preco = int(input("insira o preço do produtor numer0: " + str(i)))
    lista = []
    lista.append(preco)
    d.update({prod: lista})

for prod,preco in d.items():
    print (f'{prod} = {preco}')

