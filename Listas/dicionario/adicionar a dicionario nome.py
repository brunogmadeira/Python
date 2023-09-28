""" Desenvolva um código em Python que adicione em um dicionário “d” os
seguintes campos: nome, idade, endereço e telefone e mostre os dados no
final. """

d = {}
while True:
    n = str(input("nome:"))
    i = int(input("idade: "))
    e = str(input("endereço: "))
    t = int(input("telefone sem -: "))
    lista = []
    lista.append(i)
    lista.append(e)
    lista.append(t)
    d.update({n: lista})
    con = str(input("continuar: "))
    if con == "n":
        break
for i in d.items():
    print ("o cadastro numero " + str(i) , d.get(str(i)))