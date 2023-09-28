""" Em um script Python, crie uma lista vazia, que seja preenchida com
notas de 3 alunos, após demonstrar a nota mais alta, a nota mais baixa,
a média geral de notas, além de ordenar a lista de forma crescente. """

lista=[]

for i in range (3):
    n = float(input("Digite o valor da nota do aluno numero " +str(i+1)+" : "))
    lista.append(n)

maior = max(lista)
menor = min(lista)
media = (sum(lista)/3)
lista.sort(reverse=False)


print ("O valor de todas notas tiradas em ordem decrescente: ", lista[0],lista[1], lista[2] )
print ("O valor de todas notas tiradas em ordem crescente: ", lista[2],lista[1], lista[0] )
print ("A maior nota tirada foi de: {}".format(maior))
print ("A menos nota tirada foi: {}".format(menor))
print ("A media de todas a notas ficou: {:.1f}".format(media))

