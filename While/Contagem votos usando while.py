""" 8) Em uma eleição existem quatro candidatos. Os votos são informados por meio
de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte
codificação:
- 1, 2, 3, 4 = voto para os respectivos candidatos;
- 5 = voto nulo;
- 6 = voto em branco;
Elabore um script em linguagem Python que leia o código do candidato em um
voto. Calcule e mostre:
- total de votos para cada candidato;
- total de votos nulos;
- total de votos em branco; 
para fechar o programa utilizar o voto = 0"""

voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
nulo= 0
branco = 0
voto = 1

print ("*"*50)
print("Escolha o seu candidato a partir do numero dele: ")
print("-(1)Bolsonaro")
print("-(2)Lula ")
print("-(3)Aecio ")
print("-(4)Temer ")
print("-(5)Nulo ")
print("-(6)Branco")
print("-(0)Fechar contador")
print ("*"*50)

while voto != 0:
    voto = int(input("Escolha qual candidato deseja votar: "))
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    elif voto == 4:
        voto4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
print("A quantidade de votos em cada canditado foi de:\n Primeiro candidato = {}\n Segundo candidato = {}\n Terceiro candidato = {}\n Quarto candidato = {}\n Nulos = {}\n brancos = {}".format(voto1,voto2,voto3,voto4,nulo,branco))