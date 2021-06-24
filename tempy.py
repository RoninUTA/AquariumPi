
#!/usr/bin/python
import os
import time
import sys

# DS18B20 driver loaded
# make sure to add the following line to /boot/config.txt in overlay section
# dtoverlay=w1-gpio
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#input temperature sensor serial code from /sys/bus/w1/devices

serialCode = "28-0000066f633e"
sensorOutputFile='/sys/bus/w1/devices/'+serialCode+'/w1_slave'
# print sensorOutputFile
# pulling raw temperature, returns lines to temp_raw
def temp_raw():
        f=open(sensorOutputFile, 'r')
        lines = f.readlines()
        f.close()
        return lines

# error check from sensor
# error check from sensor
def read_temp():
        lines = temp_raw()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = temp_raw()
        # determine temperature in C/F
        temp_output = lines[1].find('t=')
        if temp_output != -1:
                temp_string = lines[1].strip()[temp_output+2:]
                temp_c = float(temp_string)/1000.0
                temp_cRnd = round(temp_c, 2)
                temp_f = temp_c * 9.0 / 5.0 + 32
                temp_fRnd = round(temp_f, 2)
                compTemp="Aquarium Temp: " + str(temp_cRnd) + " C" + " / "  + str(temp_fRnd) + " F"
                return compTemp

print (read_temp())
sys.exit()

