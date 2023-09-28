c = {}
d = {}

while True:
    quer = input("Quer utilizar alguma ferramenta? (s) para sim ou (n) para não: ")
    
    if quer == "s" or quer == "S":
        
        while True:
            print ("Aqui voce pode adicionar produtos novos\nOu mudar as informações de algum produto por meio de seu nome\n")
            l = []
            nome = input("Qual o nome do produto: \n")
            qnt = int(input("Qual a quantidade do produto existente:\n"))
            preço = float(input("Qual o preço do produto:\n"))
            l.append(qnt)
            l.append(preço)
            d.update({nome:l})
            c = input('Voce deseja continuar com a adição/mudanças de produtos? (S) para sim , (N) para não!\n')
            if c == "N" or c == "n":
                print ("Voce fechou o programa de adicão/mudança e produtos!\n")
                break

        while True:
            veri = input("Deseja verificar a quantidade de um produto? \n")
            if veri == "S" or veri == "s":
                veri2 = input("Qual o nome do produto voce deseja verificar? \n")
                print (d.get(veri2))
            else:
                break
            

        while True:
            todos = input("Deseja saber todos os produtos que existem em estoque?, (S) para sim ou (N) para no: ")
            if todos == "S" or todos == "s":
                print (d)
            else:
                break
                
        while True:
            remov = input("Deseja remover algum produto, (S) para sim ou (N) para não: ")
            if remov == "S" or remov == "s":
                qremov = input("Qual o nome do produto deseja remover: ")
                d.pop(qremov)
                print ("OS produtos que sobraram foram: " , d)
            else:
                break
    else:
        print("Programa fechado")
        break           
