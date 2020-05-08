from novo_cadastro import Novo_Cadastro
from valida_cadastro import Valida_Usuario 
from time import sleep

print("***SEJA BEM VINDO AO SISTEMA***")

sleep(1)    
while(1):
    print("Você deseja:\n1)Acessar o sistema\n2)Cadastrar novo usuário")
    INPUT = int(input("Digite a sua opção: "))
    if INPUT == 1:
        Valida_Usuario()
    if INPUT ==2:
        Novo_Cadastro()
    else:
        print("Digite uma opção válida")
    

    
