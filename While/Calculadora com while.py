"""Calculadora com saida no 5"""
opr = ""
while True:
    opr= int(input("Digite qual opção voce quer, 1=adição, 2 = subtração, 3 = multiplicação, 4 = divisão, 5 = saida\n" ))
    if opr ==5:
        print ("Você fechou o progama de calculo")
        break
    num1,num2= map(float,input("Digite o primeiro e o segundo valor, separados por um espaço: \n").split(" "))
    if opr == 1:
        conta = (num1 + num2)
        op = "adição"
    elif opr == 2:
        op = "subtração"
        conta = (num1 - num2)
    elif opr == 3:
        op = "multiplicação"
        conta = (num1 * num2)
    elif opr == 4:
        op = "divisão"
        conta = (num1 / num2)
    print ('O restultado da sua {} foi {:.2f}'.format(op,conta)) 
    
    