""" 5 valores lista invertido e normal """
lista = []

for i in range(5):
    n = int(input("Digite o valor em numeros inteiro para a lista numerada em" +str(i) + ":"))
    lista.append(n)
print (lista , lista[::-1])