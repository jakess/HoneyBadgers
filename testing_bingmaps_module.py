#trash file for testing bingtraffic

from bingmaps import *

lat_2=40
lon_1=-70
lat_1=30
lon_2=-60

bing = BingTraffic()

response = bing.get_traffic(lon_1,lat_1,lon_2,lat_2)
print response
