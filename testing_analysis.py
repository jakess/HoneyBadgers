from parse import *
from analysis import *
from gmaps import Directions
import time
api = Directions()

commuter_file = 'data/merck_zip_data'
commuters = get_commuter(commuter_file)
dest_zip = '19038'

def test():
  zip_hist_cnt = zip_hist(commuters)
  #get all zip codes 
  zips = zip_hist_cnt.keys()
  #turn dict into list
  mos_com = zip_hist_cnt.most_common()
  #get directions for each person
  i=0
  total_time_seconds = 0
  while i < len(zips):
    print i
    zipcode = str(mos_com[i]).split("'")[1]
    num_in_zipcode = int(str(str(mos_com[i]).split(")")[1]).split(", ")[1])

    route = api.directions(zipcode, dest_zip)
    dict_route = get_directions(route)

    #increment to next zipcode 
    i+=1

    #total time is time it took for zipcode * number of commuters
    # in that zipcode (num of people can be thought of as a weight)
    total_time_seconds+=get_time(dict_route)*num_in_zipcode
    
    #to try to not hit the rate limit
    time.sleep(.6)
    
  return total_time_seconds
  
def get_time(dict_route):
  '''
  Function to get time to a dest
  Takes dict (from google maps) with information for single route
  Returns time, in seconds, the route took
  '''
  return dict_route['legs']['duration']['value']


