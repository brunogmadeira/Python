clientes = {}
clientesa = {}
carros = {}
carrosa = {}



while True:

    print ("*"*40)
    print ("   -MENU DE OPERAÇÕES PARA LOCADORAS-")
    print ("1-Cadastrar clientes")
    print ("2-Adicionar ou remover veiculos da frota")
    print ("3-Ver veiculos disponiveis para aluguel")
    print ("4-Ver quais veiculos ja estão alugados")
    print ("5-Clientes com veiculos alugados")
    print ("6-Aluguel de veiculos")
    print ("7-Devolução de veiculos")
    print ("*"*40)

    op = input("Escolha uma das opções de operação, e caso desejar sair digite (fechar): ")

    #cadastro de clientes
    if op == "1":
        while True:
            l = []
            cont = input("Bem vindo ao cadastro de clientes, necesario (Nome completo, CPF e telefone). Caso desejar sair da tela digite ""sair"", senão digite ""continuar"":  ")
            if cont == "continuar":
                nome = input("Digite o nome do cliente: ")
                cpf = input("Digite o CPF do cliente: ")
                tel = input("Digite o telefone do cliente: ")
                l.append(cpf)
                l.append(tel)
                clientes.update({nome:l})
            else:
                break

    #Adicionar veiculos na frota
    elif op == "2":
        while True:
            l=[]
            cont = input("Bem vindo ao cadastro de carros, (Marca, Modelo e Ano). Caso desejar sair da tela digite ""sair"", senão digite ""continuar"": ")
            if cont == "continuar":
                marca = input("Qual a marca do carro: ")
                modelo = input("QUal o modelo do carro: ")
                ano = input("Qual o ano do carro: ")
                l.append(marca)
                l.append(ano)
                carros.update({modelo:l})
            else:
                break

    #Veiculos disponiveis para aluguel
    elif op == "3":
        cont = input("Deseja ver os veiculos disponiveis para aluguel, (continuar) para ver ou (sair) para sair da tela: ")
        if cont == "continuar":
            print (carros)
        else: 
            continue

    #Veiculos que ja estão alugados
    elif op == "4":
        cont = input("Deseja ver quais veiculos ja estão alugados, (continuar) para ver ou (sair) para sair da tela: ")
        if cont == "continuar":
            print (carrosa)
        else:
            continue

    #Clientes que tem algum carro alugado no nome
    elif op == "5":
        cont = input("Deseja ver quais clientes tem um veiculo alugado em seu nome: (continuar) para ver ou (sair) para sair da tela: ")
        if cont == "continuar":
            print (clientesa)
        else:
            continue

    #realizar aluguel de um veiculo
    elif op == "6":
        cont = input("Deseja realizar o aluguel de um veiculo: (continuar) para realizar ou (sair) para sair da tela: ")
        if cont == "continuar":
            l = []
            vei = input("Qual veiculo deseja alugar: ")
            cli = input("Qual o nome do cliente que ira alugar o carro: ")
            temp = int(input("Quantos dias o cliente ficara com o veiculo: "))
            valor = 150*temp
            carro = vei
            valores = carros.pop(carro)
            carrosa[carro] = valores
            print (carrosa)
            print (carros)



    #devolução de veiculos
    elif op == "7":
        cont = input("Deseja realizar a devolução de algum veiculo ja alugado?: (continuar) para sim, ou (sair) para não: ")
        if cont == "continuar":
            print ("a")
        else:
            continue



    elif op == "fechar":
        break