""" Elabore um script em linguagem Python que, dados dois inteiros x e y,
retorna uma lista com todos os valores entre x e y (inclusive), considerando x <
y. Exemplos x = 2, y = 6, resultado = [2, 3, 4, 5, 6] """

lista = []

x = int(input('digite o valor do x: \n'))
y = int(input('digite o valor do y: \n'))
y = y+1
print ("*"*30)
for valor in range (x, y):
    lista.append(valor)
print (lista)