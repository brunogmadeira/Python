notas = (100,50,20,10,5)
i =0
valor = int(input("Qual o valor a sacar: "))
while i < len(notas):
    qntd = int(valor/notas[i])
    valor = valor%notas[i]
    if qntd != 0:
        print (qntd, notas[i])
    i = i + 1
