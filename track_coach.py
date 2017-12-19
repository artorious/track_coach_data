#!/usr/bin/env python3
""" Track Coach Data 
A play on files and working the data files, 
text files holding athletes track records.
    * Process the data from file into lists
    * Transform and display data in the lists.

TODO: Look up top three fastest times for each athlete
"""

# Fix non-uniformity in the athletes data to enable sorting
def sanitize(time_string):
    """(str) -> str
    Takes as input <time_string>, a string from each of the athletes's lists.
    Processes the string to replace any dashes or colons found with a period. 
    Returns the sanitized string
    """
    if '-' in time_string:
        splitter = '-'
        (mins, secs) = time_string.split(splitter)

    elif ':' in time_string:
        splitter = ':'
        (mins, secs) = time_string.split(splitter)

    else:
        return time_string
        
    return '{0}.{1}'.format(mins, secs)

# Process each file, creating a list for each athlete’s data
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

#  Re-assign each transformend (sanitized & sorted) list.
james = sorted([sanitize(each_time) for each_time in james])
julie = sorted([sanitize(each_time) for each_time in julie])
sarah = sorted([sanitize(each_time) for each_time in sarah])
mikey = sorted([sanitize(each_time) for each_time in mikey])

print('James: {0}\nJulie: {1}\nSarah: {2}\nMikey: {3}'.format(
    james, julie, sarah, mikey
))

#TODO:
print('Top 3 - Three fastest times for each athlete')