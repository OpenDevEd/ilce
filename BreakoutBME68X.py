import time
from breakout_bme68x import BreakoutBME68X
import pimoroni_i2c

PINS_PICO_EXPLORER = {"sda": 4, "scl": 5}

i2c = pimoroni_i2c.PimoroniI2C(**PINS_PICO_EXPLORER)
bme = BreakoutBME68X(i2c)

while True:
    temperature, pressure, humidity, gas, status, _, _ = bme.read()
    heater = "Stable" if status else "Unstable" # & STATUS_HEATER_STABLE 
    print("{:0.2f}c, {:0.2f}Pa, {:0.2f}%, {:0.2f} Ohms, Heater: {}".format(temperature, pressure, humidity, gas, heater))
    temp = str(round(temperature,1))
    press = str(round(pressure/100,1))
    humid = str(round(humidity,1))
    time.sleep(5.0)
