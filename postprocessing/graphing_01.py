# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 19:37:04 2014

@author: tyler
"""

from loadGroupStats import *
import numpy as np


dataFiles = ['westpoint_commute_filtered_01', 'whitehouse_commute_filtered_01', 
             'kenilworth_commute_filtered_01', 'bridgewater_commute_filtered_01'] 
graphTitles = ['Westpoint Commute Time', 'Whitehouse Commute Time',
               'Kenilworth Commute Time','Bridgewater Commute Time']
stupidColors = [['r','r','r','r','r','r','r','r','r','r','r'],
                ['g','g','g','g','g','g','g','g','g','g','g'],
                ['b','b','b','b','b','b','b','b','b','b','b']
               ] 
graphColors = ['r','g','b','orange']

# print overall average commute w/o highlighted 
for dataFile, graphTitle, graphColor in zip (dataFiles, graphTitles, graphColors):
    groups,groupStats = loadGroupStats('../filteredData/' + dataFile)
    x = []
    y = []
    error = []
    for group in groupStats:
        x.append(group)
        y.append(groupStats[group][0])
        error.append(groupStats[group][3])
    plt.figure(graphTitle)
    plt.bar(np.arange(len(x)),y, yerr=error, align='center',
            color=graphColor, ecolor='k',linewidth=2)
    plt.xticks(np.arange(len(x)),x)
    plt.ylabel('Average Commute Time (mins)')
    plt.title(graphTitle)
    plt.axis([-1,12,0,120])
    
    # print graphs
    plt.savefig('../publishing/' + dataFile + '.png', bbox_inches='tight')
    plt.savefig('../publishing/' + dataFile + '.pdf', bbox_inches='tight')
    
# attempt to automate file output     
#    saveFile = open('../publishing/' + dataFile + '.txt', 'w+')        
#    saveFile.write('Average Group Commute Time: ' + str(np.average(y)) + ' mins \n' +
#                   'Standard Deviation of Commute Times: ' + str(np.std(y)) + ' mins \n' +
#                   'Max Average Group Commute Time: ' + str(max.std(y)) + ' mins \n' +
#                   'Min Average Group Commute Time: ' + str(min.std(y)) + ' mins \n'
#                   )
#    saveFile.close()
                   
    plt.show()
    print graphTitle
    print 'Average Employee Commute Time:', np.average(y), ' mins'
    print 'Standard Deviation of Commute Times:', np.std(y), ' mins'
    print 'Max Average Employee Commute Time:', max(y), ' mins'
    print 'Min Average Employee Commute Time:', min(y), ' mins\n'
    
    for org, stats in groupStats.iteritems(): 
        print 'Statistics for Organization:', org
        print 'Average Employee Commute Time: ',stats[0], ' mins'
        print 'Standard Deviation of Commute Time: ',stats[3], ' mins'
        print 'Max Employee Commute Time: ', stats[1], ' mins'
        print 'Min Employee Commute Time: ', stats[2], ' mins \n'
    

# print overall average commute w/o highlighted 
#groupIndex = 0
#for dataFile, graphTitle, graphColor in zip (dataFiles, graphTitles, stupidColors):
#    groups,groupStats = loadGroupStats('../filteredData/' + dataFile)
#    x = []
#    y = []
#    error = []
#    for group in groupStats:
#        x.append(group)
#        y.append(groupStats[group][0])
#        error.append(groupStats[group][3])
#    
#    
#    for index, org in enumerate(groups): 
#        stupidColors = [['r','r','r','r','r','r','r','r','r','r','r','r'],
#                ['g','g','g','g','g','g','g','g','g','g','g','g'],
#                ['b','b','b','b','b','b','b','b','b','b','b','b']
#               ] 
#        plt.figure(graphTitle)
#        stupidColors[groupIndex][index] = 'w'
#        barlist = plt.bar(arange(len(x)),y, yerr=error, align='center',
#            color=stupidColors[groupIndex], ecolor='k',linewidth=2,)
#        plt.xticks(arange(len(x)),x)
#        plt.ylabel('Average Commute Time (mins)')
#        plt.title(graphTitle)
#        plt.axis([-1,12,0,120])
#        plt.show()
#    groupIndex = groupIndex + 1        
        
    




    
    


