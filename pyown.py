#!usr/bin/python
import pyowm
 
owm = pyowm.OWM('4c3d0fef942b849e70d9e84552d7ab37')
observation = owm.weather_at_place('Cape Coast')
w = observation.get_weather()

#print (w.get_wind())
#print (w.get_humidity())
print (w.get_temperature()['temp max')

