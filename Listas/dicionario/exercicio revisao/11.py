""" Em um script Python com duas listas de três elementos com números
inteiros, crie uma nova lista onde cada elemento é a soma dos elementos de
mesma posição nas duas primeiras listas.
Exemplo: Lista1 = [1, 4, 6] Lista2 = [2, 4, 3] Lista_resultante = [3, 8, 9] """

lista1 = []
lista2 = []
lr = []

for i in range (1,4):
    n = int(input("Digite o valor, numero" + str(i) + ": \n"))
    lista1.append(n)
    n2 = int(input("Digite o valor que sera somado, numero:" + str(i) + ": \n"))
    lista2.append(n2)

for i in range (0,3):
    soma = lista1[i] + lista2[i]
    lr.append(soma)

print ("a soma das duas listas seguintes:\n" , lista1 , lista2)
print ("o total da soma acima foi de: ", lr )