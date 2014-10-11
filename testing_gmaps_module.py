from gmaps import Directions 
import json
from parse import *
api = Directions()
 
results = api.directions("Temple University,  Philadelphia PA","2296 Byecroft Rd, New Hope PA")
#print json.dumps(results, sort_keys=True, indent = 4, separators=("'",': '))

#test of input files library
dest_zip_file = 'data/merck_work_zip'
commuter_file = 'data/merck_zip_data'
#get zip codes of destinations 
dest_zip = get_dest_zip(dest_zip_file)

#get list of all commuters
commuters = get_commuter(commuter_file)
print commuters
