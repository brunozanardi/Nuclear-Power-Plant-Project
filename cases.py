from time import sleep
import pot_readings as pr
import Straingauge_control as st
import temperature_sensor as ts
import pressure_sensor as ps

def cases(button):
    if button==0:
        pass

    if button==1:
        print("Preparando para ajustar o potenciômetro de temperatura\n")
        sleep(2)
        print("Ajuste a tensão para ficar entre 1.3 V e 1.5 V\n")
        while True:
            voltage_1 = pr.channel1()
            if 1.3<voltage_1<1.5:
                print("Valor Ajustado")
                break
            else:
                sleep(1)
                print("Tensão no Potenciômetro 1: {}".format(voltage_1))

        print("Preparando para ajustar o potenciômetro de pressão")
        sleep(2)
        print("Ajuste a tensão para ficar entre 0.3 V e 0.5 V\n")
        while True:
            voltage_2 = pr.channel2()
            if 0.3<voltage_2<0.5:
                print("Valor Ajustado")
                break
            else:
                sleep(1)
                print("Tensão no Potenciômetro 2: {}".format(voltage_2))

        print("Preparando para ajustar potênciometro de carga")
        sleep(2)
        print("Ajuste a tensão para ficar entre 2.5 V e 2.8 V\n")
        while True:
            voltage_3 = pr.channel3()
            if 2.5<voltage_3<2.8:
                print("Todos os potenciômetros devidamente ajustados. Iniciando coleta de dados\n")
                button = 2
                break
            else:
                sleep(1)
                print("Tensão no Potenciômetro 3: {}".format(voltage_3))

        if button==2:
            while(1):
                temperatura= ts.temperature_sensor()
                pressao= ps.Pressure()
                altitude= ps.Altitude()
                print('Temperatura = {0:0.2f} *C'.format(temperatura))
                print('Pressão = {0:0.2f} Pa'.format(pressao))
                print('Altitude = {0:0.2f} m'.format(altitude))
                #print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
                                

