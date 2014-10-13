
from bingmaps import *
import time
import sched
import datetime

lat_2=-70
lon_1=39
lat_1=-76
lon_2=42

bing = BingTraffic()
s = sched.scheduler(time.time, time.sleep)

def run_day():
	now = datetime.datetime.now()
	stime = now.time()
	#Run forever
	while True:
		#Run everyday during 4-7pm rush hour
		if stime < datetime.time(16,0):
			stime = datetime.time(16,0)
			while stime <= datetime.time(19,0):
				#run the program every 30 minutes
				s.enterabs(stime,1, run_time, ())
				now = datetime.datetime.now()
				next_time = now + datetime.timedelta(seconds=1800)
				stime = next_time.time() 

		#Run everyday during 7-10am rush hour
		elif stime < datetime.time(7,0):
			stime = datetime.time(7,0)
			while stime <= datetime.time(19,0):
				#run the program every 30 minutes
				s.enterabs(stime,1, run_time, ())
				now = datetime.datetime.now()
				next_time = now + datetime.timedelta(seconds=1800)
				stime = next_time.time()

def run_time():
	response = 'jasdlf'
	#response = bing.get_traffic(lon_1,lat_1,lon_2,lat_2)
	#get current time
	curr_time=time.time()
	#cast time as string and remove the decimal point 
	curr_time_str=str(curr_time).split('.')[0]
	#create file name
	file_name = 'traffic_data_' +curr_time_str
	#open file and write date
	with open(file_name, 'w+') as traffic_file:
		traffic_file.write(str(curr_time)+'\n')
		traffic_file.write(response)

#start program
run_day()


