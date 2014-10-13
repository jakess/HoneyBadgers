# library file to get data from bing maps

#needed for bing maps API used in get_traffic
import urllib2
import json

class BingMaps:
	"""
	Parent class for Bing Maps python interface
	"""
	def __init__(self, API_KEY = 'AiW0a2uSO_PoOXP5nABRYRYwSPhMXUoO7iYiwSw5BSzXxjn3kXTxlkfnQ20nPKrK'):
		self.__API_KEY__ = API_KEY
		self.__URL_BASE__ = 'http://dev.virtualearth.net/REST/V1/'

class BingTraffic(BingMaps):
	"""
	Class to get traffic information from bing maps
	Child class of BingMaps
	"""

	def get_traffic(self, lon_1,lat_1,lon_2,lat_2):
		"""
		Function to get traffic conditions inside the location box specified by
		lon_1, lat_1, lon_2, lat_2
		Takes location box coordinates as integers lat_1, lon_1 and lat_2 and lon_2
		Returns json string 
		"""
		#checking input arguments
		if float(lon_1) > float(lon_2):
			print 'Error in box size. Check longitude'
			return 0
		elif float(lat_1) > float(lat_2):
			print 'Error in box size. Check latitude'
			return 0
			
		#setting up variables to use in URL
		url_traffic = 'Traffic/Incidents/'
		lat_1 = str(lat_1)
		lat_2 = str(lat_2)
		lon_1 = str(lon_1)
		lon_2 = str(lon_2)
		traffic_flag = '/true?t=2,3&'
		key = 'key='+self.__API_KEY__

		#constructing URL
		url = self.__URL_BASE__ +url_traffic+lon_1+','+lat_1+','+lon_2+','+lat_2+traffic_flag+key
		print url
				
		#sending URL and getting response
		response = urllib2.urlopen(url)
		data = json.load(response)
		dict_traffic = data
		return dict_traffic
