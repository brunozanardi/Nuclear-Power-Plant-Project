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

#def channel4():
chan4 = AnalogIn(ads, ADS.P3)
def temperature_sensor():
    while(1):
        channel4_voltage = chan4.voltage
        temperature = 1000*(channel4_voltage/12.9411)
        return temperature
        #return channel4_voltage
        #sleep(0.1)
