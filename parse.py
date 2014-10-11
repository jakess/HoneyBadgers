#!/usr/bin/env python

#Jake Version 0.1

#Library to parse the input files we are given

#assumes file looks like: <name> is <zipcode>
def get_dest_zip(dest_zip_file):
	dest_zip_file_contents = open (dest_zip_file)

	for line in dest_zip_file_contents:
		line = line.rstrip('.\n')
		line_split = line.split("is")
		dest_zip = {line_split[0]:line_split[1]}
		return dest_zip

#assumes commute file has 3 columns and a single line header
#col1 is ID number
#col2 is home zip code
#col3 is Org	
#returns dictionary with [Zip][Org][Id]	
def get_commuter(commuter_file):
	"""
	Function to get all commuters from input file commuter_file
	Takes input file
	Assumes commute file has 3 columns and a single line header
	col1 is ID number
	col2 is home zip code
	col3 is Org	
	Returns dictionary with [Zip][Org][Id]	

	"""
	#initalise output dictionary
	commuter_dict= {}
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
			#dictionary is [Zip][Org][ID]
			commuter_dict.update({zips:{orgs:ids}})			
	return commuter_dict
