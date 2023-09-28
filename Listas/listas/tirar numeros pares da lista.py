lista = []
print  ("Sistema para tirar numeros pares")
n1 = int(input("digite o valor onde ira começar a lista:"))
n2 = int(input("digite o valor onde ira terminar a lista: "))
n2 = n2+1
for i in range(n1,n2):
    if i %2 == 1:
        lista.append(i)
     
print (lista)
