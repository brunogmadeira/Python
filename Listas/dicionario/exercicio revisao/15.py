""" Elabore um script que crie um dicionário na qual cada chave seja um
caractere e seu valor seja o número de vezes que o caractere aparece na frase.
Exemplo:
"Digite uma frase para contar as letras:“ – eu sei
Resposta {'e': 2, 'u': 1,
' ': 1, 's': 1, 'i': 1} """

d= {}

frase = input("digite uma frase")
lista = list(frase)

for letra in lista:
    d[letra] = lista.count(letra)

print(d) 
