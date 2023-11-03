import pandas as pd
import matplotlib.pyplot as plt
import time


while True:
	#kiolvasni az adatokat
	updated_data = pd.read_excel('/home/zolika/Adafruit_Python_BME280/weather.xlsx')
	
	#torolni az elozo diagramot (mindig uj felületre dolgozzon)
	plt.clf()
	
	#adatsorok elnevezese
	x = updated_data['time']
	y1 = updated_data['temperature']
	y2 = updated_data['humidity']
	
	#abrazolni az adatokat
	plt.plot(x, y1, label = 'Temperature')
	plt.plot(x, y2, label = 'Humidity')
	plt.title('Projektfeladat')
	
	# 'Y' tengely felosztas
	plt.ylim(15,60)
	plt.yticks(range(15, 60 +1, 1))
	
	plt.legend(loc='upper left')
	plt.xticks(rotation=90)
	
	#adatok frissitese (x) masodpercenkent
	plt.pause(10)
	
 
