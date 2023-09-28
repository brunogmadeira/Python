lista=[]

for i in range (3):
    n = float(input("Digite o valor da nota do aluno numero " +str(i+1)+" : "))
    lista.append(n)

maior = max(lista)
menor = min(lista)
media = (sum(lista)/3)
ccres = lista.sort(reverse=False)
cres = ccres
ddesc = lista.sort(reverse=True)
desc = ddesc
 
print (cres)