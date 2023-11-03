from Adafruit_BME280 import *
import datetime
import time
from datetime import date
import openpyxl
from openpyxl import load_workbook

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

# excel betoltese es a munkafuzet kivalasztasa	
wb = openpyxl.load_workbook('/home/zolika/Adafruit_Python_BME280/weather.xlsx')
sheet = wb['adatok']


try:
	while True:
		
		#adatok olvasasa szenzorbol es kijelzese, illetve az ido megjelenitese
		degrees = round(sensor.read_temperature(),2)
		pascals = round(sensor.read_pressure(),2)
		dhectopascals = pascals / 100
		humidity = round(sensor.read_humidity(),2)
		today = date.today()
		now = datetime.datetime.now().time()
		formatted_time = now.strftime("%H:%M")
		
		print (today)
		print (formatted_time)
		print ('Temp      = {0:0.3f} deg C'.format(degrees))
		print ('Pressure  = {0:0.2f} hPa'.format(dhectopascals))
		print ('Humidity  = {0:0.2f} %'.format(humidity))
		
		#adatok munkafuzetbe toltese
		row = (formatted_time, degrees, humidity)
		sheet.append(row)
		
		#munkafuzet mentese
		wb.save('/home/zolika/Adafruit_Python_BME280/weather.xlsx')
		
		#idozites
		time.sleep(60)
		
finally:  ''
