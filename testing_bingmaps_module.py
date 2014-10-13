#trash file for testing bingtraffic

from bingmaps import *
lat_2=-70
lon_1=39
lat_1=-76
lon_2=42

bing = BingTraffic()

response = bing.get_traffic(lon_1,lat_1,lon_2,lat_2)
print response
