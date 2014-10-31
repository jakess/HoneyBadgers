#!/usr/bin/env python

#Library to parse the input files we are given

'''
    EDITS: Changed get_commuter to ordereddict, closed any opened files (10/25)
    EDITS: Change get_commuter to list with the following format: 
    EDITS: Changed get_commuter to output integers when possible 
    i.e. zips and id numbers. 
    EDITS: Change get_commuters to output str for zips due to loss of zeros 
    
'''

#Import needed for get_directions
import json
import collections
from collections import OrderedDict

def get_dest_zip(dest_zip_file):
    """
    Function to get the destation zip codes out of the given files
    Takes input file destination 
    Assumes input file looks like: <name> is <zipcode>
    Returns dictionary of [Name of Place][Zip]
    """
    dest_zip_file_contents = open (dest_zip_file)
    
    dest_zip= {}
    for line in dest_zip_file_contents:
        line = line.rstrip('.\n')
        line = line.rstrip(' ')
        line_split = line.split("is")
        #remove trailing white space
        line_split[0] = line_split[0].rstrip(' ')
        #remove preceding white space
        line_split[1] = (line_split[1].rsplit(' '))[1]
        #add to dictionary 
        dest_zip.update({line_split[0]:line_split[1]})
    dest_zip_file_contents.close()
    return dest_zip

def get_commuter(commuter_file):
    """
    Function to get all commuters from input file commuter_file
    Takes input file
    Assumes commute file has 3 columns and a single line header
    col1 is ID number
    col2 is home zip code
    col3 is Org    
    Returns list with [Id,Org,Zip]    

    """
    #initalise output dictionary
    commuter_list = []
    commuter_file_contents = open (commuter_file)
    for line in commuter_file_contents:
        #remove new line character
        line = line.rstrip('\n')
        line_split = line.split(',')
        #remove header
        if line_split[0] == 'Employee Id':
            a = 1
        #remove empty lines
        elif line_split[0] == "":
            a=1
        else:
            #place person in dictionary
            zips = line_split[1]
            orgs = line_split[2]
            ids = line_split[0]
            #dictionary is [ID][Org][Zip]
            commuter_list.append([int(ids),orgs,zips])            
    commuter_file_contents.close()
    return commuter_list
    

def get_directions(json_directions):
    """
    Function takes the json message from gmaps.Directions and turns it into a python dictionary 
    Takes json message from gmaps.Directions
    Returns python dictionary with all information from the json message
    """

    #place json response into dictionary
    dict_results = json.loads(json.dumps(json_directions,sort_keys=True))[0]
    #place legs (where distance, duration, and waypoints are) into dict
    legs_dict = json.loads(json.dumps(dict_results['legs'],sort_keys=True))[0]
    #place back into master dict
    dict_results['legs']=legs_dict

    #place the steps into dictionary 
    steps_dict={}
    i=0
    #loop over all steps (they are lists) and place into a steps_dict
    while i < len(dict_results['legs']['steps']):
        step_n = json.loads(json.dumps(dict_results['legs']['steps'],sort_keys=True))[i]
        steps_dict.update({i:step_n})
        i+=1
    #place steps_dict into master dict
    dict_results['legs']['steps']=steps_dict

    return dict_results

def get_polyline(dict_results):
    '''
    Functions takes dict_results from get_directions and returns the overview polyline as a string 
    '''
    dict_polyline = dict_results['overview_polyline'][u'points']
    return str(dict_polyline)

