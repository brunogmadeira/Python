"Listas"
""" 2) Desenvolva um script em linguagem Python que peca as quatro notas de 10
alunos, calcule e armazene num vetor a media de cada aluno, imprima o
nmeero de alunos com media maior ou igual a 7. """
lista = []
for i in range (1,5):
    n1 = float(input("Digite a primeira nota do aluno " + str(i)+ ": " ))
    n2 = float(input("Digite a segunda nota do aluno " + str(i)+ ": "))
    n3 = float(input("Digite a terceira nota do aluno " + str(i)+ ": "))
    n4 = float(input("Digite a quarta nota do aluno " + str(i)+" : "))
    media = (n1 + n2 + n3 + n4)/4
    lista.append(media)

print ("As notas dos alunos foram ", lista)