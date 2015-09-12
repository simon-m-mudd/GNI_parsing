# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:03:39 2015

@author: smudd
"""

import csv
import os

def RemoveEscapeCharacters(line):
    line = line.rstrip().replace('\\n', '\n')
    line = line.rstrip().replace('\\b', '\b') 
    line = line.rstrip().replace('\\r', '\r')  
    line = line.rstrip().replace('\\t', '\t')  
    line = line.rstrip().replace('\\n', '\n')  
    line = line.rstrip().replace('\\f', '\f')  
    line = line.rstrip().replace('\\v', '\v') 
    
    # this last one deals with the infuriating special case of \b
    line = line.rstrip().replace('\x08', '\\b')     
    return line

def World_bank_reader():
    
    cwd = os.getcwd()    
    print "cwd: " + cwd
    print "ls: "
    print os.listdir(cwd)

    fname = 'gni_unix.csv'

    if os.access(fname,os.F_OK):
        this_file = open(fname, 'r')
        
        # get all the data
        lines = this_file.readlines()
        
        # split the first line to find out what columns are the specific entries
        line = lines[0]  
        line = RemoveEscapeCharacters(line)
        split_line = line.split(",")
        
        print split_line
        
        # get the indices for the different elements
        year_index = split_line.index("Year")
        GNI_caput_index = split_line.index("GNI.caput")
        Country_name_index = split_line.index("Country.Name")
        Country_code_index = split_line.index("Country.Code")
        
        print str(year_index) + " " + str(GNI_caput_index) + " " + str(Country_name_index) + " " + str(Country_code_index)

        # now get the list of DEM prefixes
        for line in lines:
            this_line = line.split(",")
            #print this_line   

            
if __name__ == "__main__":
    World_bank_reader() 