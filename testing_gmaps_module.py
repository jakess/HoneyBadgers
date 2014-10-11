from gmaps import Directions 
import json
from parse import *
api = Directions()
 
results = api.directions("Temple University,  Philadelphia PA","2296 Byecroft Rd, New Hope PA", "walking")
#place json response into dictionary
dict_results = json.loads(json.dumps(results,sort_keys=True))[0]
#place legs (where distance, duration, and waypoints are) into dict
legs_dict = json.loads(json.dumps(dict_results['legs'],sort_keys=True))[0]
#place back into master dict
dict_results['legs']=legs_dict


#ONLY RETURNS ONE LEG DOESNT WORK
#place the steps into dictionary 
steps_dict = json.loads(json.dumps(dict_results['legs']['steps'],sort_keys=True))[0]

#print dict_results
#print json.dumps(results, sort_keys=True, indent = 4, separators=("'",': '))
#print json.dumps(dict_results['legs'], sort_keys=True, indent = 2, separators=("'",': '))

#test of input files library
dest_zip_file = 'data/merck_work_zip'
commuter_file = 'data/merck_zip_data'
#get zip codes of destinations 
dest_zip = get_dest_zip(dest_zip_file)
print dest_zip
#get list of all commuters
commuters = get_commuter(commuter_file)
#print commuters
