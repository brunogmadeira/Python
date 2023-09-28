""" 13 - Desenvolver um programa que leia a altura de 4 pessoas. Este programa
deverá calcular e mostrar:
a. A menor altura do grupo;
b. A maior altura do grupo;
c. Em uma lista cada um dos dados de entrada. """
l = []

for i in range(0,5):
    a = int(input("digite a altura em centimetros, pessoa" +str(i) + ": "))
    l.append(a)
menor = min(l)
maior = max(l)

print (l)
print (maior)
print (menor)
