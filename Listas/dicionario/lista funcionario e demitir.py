""" Elabore um script em linguagem Python, utilizando Dicionários, que
contenha 4 funcionários, com o índice numérico e seu nome. Em seguida,
solicite do usuário demitir um dos funcionários conforme o número de
cadastro e mostre na tela os funcionários restantes. """

d = {}

for i in range (0,2):
    f = str(input("Nome do funcionario: "))
    ind = int(input("Indice do funcionario: "))
    d.update({ind: f})

print  ("Funcionarios cadastrados: ", d)

rmv = input("deseja demitir um funcionaio? (s) para e (n) para não: \n")

copia = dict(d)

if rmv == "s":
    cod = int(input("Qual o codigo do funcionario que deseja remover: \n"))
    d.pop(cod)
    print ("funcionario", copia.get(cod) , "removido")
    
print ("os funcionarios que sobraram foi: ", d)   
