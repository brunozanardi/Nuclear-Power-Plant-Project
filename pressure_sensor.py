import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()
def Pressure():
    while(1):
        return sensor.read_pressure()
def Temperature():
    while(1):
        return sensor.read_temperature()
def Pressao_nivelmar():
    while(1):
        return sensor.read_sealevel_pressure()
def Altitude():
    while(1):
        return sensor.read_altitude()
