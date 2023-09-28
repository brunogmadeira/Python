
import time
import os 
id == ""
while True:
    smenu = "*"
    print (smenu * 30)
    print ("CALCULO DE GRANDEZAS ELETRICAS")
    print (smenu * 30)
    print ("1. Tensão em volt.")
    print ("2. Resistencia em Ohm.")
    print ("3. Corrente em ampere.")
    print ("4. Para fechar o programa.")
    print (smenu * 30)
    id = int(input("Qual grandeza deseja calcular, digite o id dela: \n"))
    if id == 4:
        print ("Voce fechou o programa")
        break
    if id == 1:
        r,i = map(float,input("Qual o valor da resistencia e corrente (Separe os valores com um espaço): ").split(" "))
        conta = r*i
        print ("O resultado da sua conta foi : {:.2f}".format(conta))
        print (" ")
        print ("Esperando reabrir o programa")
        time.sleep(2)
        
    elif id == 2:
        u,i= map(float,input("Qual o valor da tensão e da corrente (Separe os valores com espaço): ").split(" "))
        conta = u/i
        print ("O resultado da sua conta foi : {:.2f}".format(conta))
        print (" ")
        print ("Esperando reabrir o programa")
        time.sleep(2)
    elif id == 3:
        u,r= map(float,input("Qual o valor da tensão e da ressistencia (Separe os valores com espaço): ").split(" "))
        conta = u/r
        print ("O resultado da sua conta foi : {:.f}".format(conta))
        print (" ")
        print ("Esperando reabrir o programa")
        time.sleep(2)





