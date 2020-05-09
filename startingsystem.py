from time import sleep
import cases as cs
import button as bt

def Starting_System():

    print("***SISTEMA LIGADO***")
    print("APERTE O BOTÃO PARA INICIAR")
    i=0

    try:
        while (1):
            
            botao = bt.button()
            cs.cases(i)
            while cs.cases(i)==False:
                i= i+1
            if botao == 0:
                i = i+1
            

    except ValueError:
        print("Erro de leitura")
    finally:
        GPIO.cleanup()
    
