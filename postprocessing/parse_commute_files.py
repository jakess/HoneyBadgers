from numpy import *
set_printoptions(threshold=nan)

def parseGroups(filename):
    inputfile = filename
    #inputfile = '../data/westpoint_commute'
    
    # load array of employee id codes 
    emp = genfromtxt(inputfile, delimiter=',',
                              dtype=None,
                              skip_header=1,usecols=(0))
                              
    # load array of organizations and filer "org" 
    org = genfromtxt(inputfile, delimiter=',',
                     dtype=None,
                     skip_header=1,usecols=(1))
    
    for index in range(0, len(org)):
        org[index] = org[index][4:]
    #print org
    
    # load array of distances and filter "mi"
    dis = genfromtxt(inputfile, dtype=None, 
                     delimiter=',',
                     skip_header=1, usecols=(4))           
    for index in range(0, len(dis)): 
        row = str(dis[index]).split()
        m = 0
        ft = 0
        for i, cell in enumerate(row): 
            if cell == 'mi':
                m = float(row[i-1])
            if cell == 'ft': 
                ft = float(row[i-1])
        dis[index] = m + ft/5280 
    
    # load array of durations and filter text
    dur = genfromtxt(inputfile, delimiter=',',
                     dtype=None,
                     skip_header=1,usecols=(3))
    for index in range(0, len(dur)): 
        row = str(dur[index]).split()
        h = 0 
        m = 0
        for i, cell in enumerate(row): 
            if cell == 'hour' or cell == 'hours':
                h = int(row[i-1])
            if cell == 'min' or cell == 'mins': 
                m = int(row[i-1])
        dur[index] = 60*h + m
    
    # recombine arrays and sort according to groups
    sortable = column_stack((org,emp,dur,dis))
    sortable = sortable[argsort(sortable[:,0])] # DONT UNDERSTAND
    return sortable
    
            
