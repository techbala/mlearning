# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:12:18 2015

@author: gbs02315
"""

data = {}

def findDistance( fWord, sWord):
    r1 = len(fWord)+1
    r2 = len(sWord)+1
    for i in range(0,r1):
        for j in range(0,r2):
            if( i == 0 or j == 0 ):
                data[i,0] = i;
                data[0,j] = j;
            else:
                ins = data[ i-1, j] + 1;
                dele = data[i, j-1] + 1;
                sub =  data[i-1, j-1] + 0 if( fWord[i-1] == sWord[j-1]) else data[i-1, j-1] + 2;
                data[i,j] = min( ins ,dele ,sub );
    print data[r1-1, r2-1]
            
            
            
findDistance('bala', 'cola')

