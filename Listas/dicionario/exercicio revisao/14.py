""" Elabore um código que leia a temperatura média de cada mês do ano e
guarde em uma lista. Com isso, efetue a média anual das temperaturas e
mostre todas que estão acima da média anual e em que mês elas ocorreram
(Ex.: 1 – Janeiro, 2 – Fevereiro, etc). """

d = {}
l = []
mess = {}
m = ["janeiro","fevereiro",'março', 'abril', 'maio']

for i in range (0,5):
    temp = int(input("digite a media de temperatura do mes " + str(i+1) + " "))
    l.append(temp)
    d.update({i: temp})
    med = sum(l)/(i+1)

        

for i in range (0,5):
    if med < d.get(i):
        mess.update({m[i]: d.get(i)})
        

print (mess)
