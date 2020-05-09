#Importanto bibliotecas
import RPi.GPIO as GPIO
from hx711 import HX711

#Iniciando o programa
#Try é uma forma de loop para proteção do sistema
def straingauge():
    try:
        GPIO.setmode(GPIO.BCM)
        bib = HX711(dout_pin=21, pd_sck_pin=20)
        err= bib.zero()
        if err:
            print('Valor invalido')
        leitura_bruta= bib.get_raw_data_mean()
        if leitura_bruta==False:
            raise ValueError('Valor lido errado')
        leitura= bib.get_data_mean()
        input('Pegue uma carga conhecida e ponha na balança. Pressione ENTER quando posicioanr.')
        try:
            massa_conhecida = input('Digite o valor em gramas da massa conhecida: ')
            valor = float(massa_conhecida)
            razão= leitura/valor
            bib.set_scale_ratio(razão)
        except ValueError:
            print('Valor impossibilita cálculo.')
        while True:
            print(bib.get_weight_mean())
            
    except(KeyboardInterrupt, SystemError):
        print('Fim do programa')
    finally:
        GPIO.cleanup()
