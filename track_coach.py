#!/usr/bin/env python3
""" Track Coach Data 
A play on files and working the data files, 
text files holding athletes track records. 
    * Look up top three fastest times for each athlete
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

# Init sanitized lists (using list comprehension)
james_sanitized = [sanitize(each_time) for each_time in james]
julie_sanitized = [sanitize(each_time) for each_time in julie]
mikey_sanitized = [sanitize(each_time) for each_time in mikey]
sarah_sanitized = [sanitize(each_time) for each_time in sarah]


# sort and display the sanitized lists 
print(sorted(james_sanitized))
print(sorted(julie_sanitized))
print(sorted(sarah_sanitized))
print(sorted(mikey_sanitized))

