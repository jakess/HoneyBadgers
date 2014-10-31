from gmaps import Directions 
import json
from parse import *
import sys
import time 

# employee_id index 
start_index = 871

# location 
loc = 'West Point, PA'
#api_key = ''
key='AIzaSyDPU2PzqF9VK5g0fSEmrTjlc9C9T65ocnY'
#key='AIzaSyB7SerbrEj9rHCoedm02nE3bImBR_j4DtU'
api = Directions(api_key=key)

# input files library
dest_zip_file = 'data/merck_work_zip'
commuter_file = 'data/merck_zip_data'

# output file library  
data_file_address = 'data/westpoint_commute'

# setup output file and create header 
output_file = open(data_file_address, 'w')
output_file.write("EMPLOYEE ID, ORGANIZATION, ZIP CODE, DURATION, DISTANCE, POLYLINE\n")

# get dict of all destination zip codes  
dest_zip = get_dest_zip(dest_zip_file)
# get dict of all commuters
commuters = get_commuter(commuter_file)

print "Retriving trip time, duration, and polyline to address:", loc

commuter_data = OrderedDict()

for index, commuter in enumerate(commuters[start_index:]):
    print 'Employee:', commuter
    # get the directions from the google api via the commuter file and destination file. 
    # and covert to dic 
    commute = api.directions( dest_zip[loc], str(commuter[2]) )
    commute_dict = get_directions(commute)
      
#     # create dictionary with employee id as key followed by [org, zip] , travel time, distance, polyline
#     commuter_data.update({commuter[0]:  [commuter[1], commuter[2],
#                                         str( commute_dict['legs']['duration'][u'text'] ),
#                                         str( commute_dict['legs']['distance'][u'text'] ),
#                                         str( commute_dict['overview_polyline'][u'points'] )
#                                         ]})
    
    # print employee id, organization, zip code, duration, distance, polyline
    output_file.write(str(commuter[0])+","+str(commuter[1])+","+str(commuter[2])
                      +","+str( commute_dict['legs']['duration'][u'text'] )+","
                      +str( commute_dict['legs']['distance'][u'text'] )+","
                      +str( commute_dict['overview_polyline'][u'points']))
    output_file.write("\n")
    time.sleep(0.5) # attempting to avoid query limits and stupid errors
output_file.close()
print "FINISHED"