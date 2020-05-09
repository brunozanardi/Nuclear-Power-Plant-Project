from novo_cadastro import Novo_Cadastro
from valida_cadastro import Valida_Usuario
from time import sleep
import startingsystem as start

print("***SEJA BEM VINDO AO SISTEMA***")

sleep(1)
attempt = False
while(1):
    try:
        print("Você deseja:\n1)Acessar o sistema\n2)Cadastrar novo usuário")
        INPUT = int(input("Digite a sua opção: "))
        if INPUT == 1:
            validacao = Valida_Usuario()
            if validacao == True:
                break
        if INPUT ==2:
            Novo_Cadastro()
        else:
            print("Digite uma opção válida")
    except:
        print("Aconteceu algum problema, tente novamente")
        
start.Starting_System()
    
