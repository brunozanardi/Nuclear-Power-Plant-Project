import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
# you can specify an I2C adress instead of the default 0x48
# ads = ADS.ADS1115(i2c, address=0x49)

def channel1():
    chan1 = AnalogIn(ads, ADS.P0)
    while(1):
        channel1_voltage = chan1.voltage
        #print("Channel 1: {} V".format(channel1_voltage))
        return channel1_voltage
        #sleep(0.1)

def channel2():
    chan2 = AnalogIn(ads, ADS.P1)

    while(1):
        channel2_voltage = chan2.voltage
        #print("Channel 2: {} V".format(channel2_voltage))
        return channel2_voltage
        #sleep(0.1)

def channel3():
    chan3 = AnalogIn(ads, ADS.P2)
    while(1):
        channel3_voltage = chan3.voltage
        #print("Channel 3: {} V".format(channel3_voltage))
        return channel3_voltage
        #sleep(0.1)

