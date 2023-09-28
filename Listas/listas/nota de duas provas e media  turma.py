p1 = []
p2 = []

for i in range (1,6):
    prova1 = float(input("Qual a nota do aluno numero "+ str(i) +" da primera prova"))
    prova2 = float(input("Qual a nota do aluno numero "+ str(i) +" da segunda prova"))
    p1.append(prova1)
    p2.append(prova2)

print ("as notas da primeira prova foram", p1 )
print ("as notas da segunda prova foram", p2)

media1 = (sum(p1)/5)
media2 = (sum(p2)/5)

print ("a media geral da primeira prova foi", media1)
print ("a media geral da segunda prova foi", media2)

if media1 >= media2:
    print ("a media foi maior na primeira prova", media1)
else: 
    print ("a media foi maior na segunda prova", media2)