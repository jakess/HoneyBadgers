
from bingmaps import *
import time
import sched
import datetime

lat_2=-70
lon_1=39
lat_1=-76
lon_2=42

bing = BingTraffic()

def run_day():
	now = datetime.datetime.now()
	stime = now.time()
	#Run forever
	while True:

	#check every hour if within time range
	sleep(3600)

		#Run everyday during 4-7pm rush hour
		while stime > datetime.time(16,0) and stime <= datetime.time(19,0):
			#run the program every 30 minutes
			run_time()
			time.sleep(1800)
			now = datetime.datetime.now()
			next_time = now + datetime.timedelta(seconds=1)
			stime = next_time.time()
				

		#Run everyday during 7-10am rush hour
		while stime > datetime.time(7,0) and stime <= datetime.time(10,0):
			#run the program every 30 minutes
			run_time()
			time.sleep(1800)
			now = datetime.datetime.now()
			next_time = now + datetime.timedelta(seconds=1800)
			stime = next_time.time()

def run_time():
	#get bing response
	response = bing.get_traffic(lon_1,lat_1,lon_2,lat_2)
	#get current time
	curr_time=time.time()
	#cast time as string and remove the decimal point 
	curr_time_str=str(curr_time).split('.')[0]
	#create file name
	file_name = 'traffic_data_' +curr_time_str
	#open file and write date
	with open(file_name, 'w+') as traffic_file:
		traffic_file.write(str(curr_time)+'\n')
		traffic_file.write(json.dumps(response, sort_keys=True, indent=4, separators=("'",':')))

#run program
run_day()


