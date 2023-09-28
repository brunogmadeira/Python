d = {}
l = []


n1 = input("QUal opimriero valor")
n2 = input("Qual o segundo valor")
n3 = input("QUal o terceiro valor")
l.append(n2)
l.append(n3)
d.update({n1:l})

qual = input("Qual nome voce quer retirar os codigos?")
""" d.values(str(qual))
 """

print (d.items())
print (d)
