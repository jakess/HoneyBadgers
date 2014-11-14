# from gmaps import Directions
# import json
# api = Directions()
#  
# results = api.directions("19020","19121")
# print json.dumps(results, sort_keys=True, indent = 4, separators=("'",': '))

from gmaps import Directions 
import json
from parse import *
api = Directions()
#a new comment!
results = api.directions("19020","19121")
 
#place json response into dictionary
dict_results = get_directions(results)
#print get_polyline(dict_results)

#print dict_results['overview_polyline']
#print json.dumps(results, sort_keys=True, indent = 4, separators=("'",': '))
#print json.dumps(dict_results['legs'], sort_keys=True, indent = 2, separators=("'",': '))
print dict_results['overview_polyline']

#test of input files library
dest_zip_file = 'data/merck_work_zip'
commuter_file = 'data/merck_zip_data'
#get zip codes of destinations 
dest_zip = get_dest_zip(dest_zip_file)
print dest_zip
#get list of all commuters
commuters = get_commuter(commuter_file)
#print commuters
