#!/usr/bin/env python3
""" Track Coach Data 
A play on files and working the data files, 
text files holding athletes track records. 
    * Look up top three fastest times for each athlete
"""

# Process each file, 
# creating a list for each athlete’s data, 
# display the lists on screen

try:
    with open('text/james.txt') as james_file:  # Open file & assign  file object
        james_data = james_file.readline()      # Read the line of data
        james = james_data.strip().split(',')   # convert data into list

    with open('text/julie.txt') as julie_file:
        julie_data = julie_file.readline()      # Read the line of data
        julie = julie_data.strip().split(',')   # convert data into list

    with open('text/mikey.txt') as mikey_file:
        mikey_data = mikey_file.readline()      # Read the line of data
        mikey = mikey_data.strip().split(',')   # convert data into list

    with open('text/sarah.txt') as sarah_file:
        sarah_data = sarah_file.readline()      # Read the line of data
        sarah = sarah_data.strip().split(',')   # convert data into list

except IOError as ioerr:
    print('File Error...', ioerr)

print(james)
print(julie)
print(sarah)
print(mikey)