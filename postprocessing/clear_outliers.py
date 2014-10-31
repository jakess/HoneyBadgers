inputFile = '../data/kenilworth_commute*' 
outputFile = '../filteredData/kenilworth_commute_filtered_01' 

data = open(inputFile, 'r') 
filteredData = open(outputFile, 'w+') 

data.readline()
outlier_count = 0
for line in data.readlines():
    row = line.split(',')
    cell = row[4].split(' ')
    f = 0
    m = 0
    for index, item in enumerate(cell): 
        if item == 'mi': 
            m = float(cell[index-1])
        if item == 'ft': 
            f = float(cell[index-1])
    if row[4] == '1' or row[4] == '2' or row[4] == '3' or m > 100:
        outlier_count = outlier_count +1
    elif (m + f/5280) <= 100:
        print line 
        filteredData.write(str(line))
print 'outliers:',outlier_count
    
