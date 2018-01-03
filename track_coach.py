#!/usr/bin/env python3
""" Track Coach Data 
A play on files and working the data files, 
text files holding athletes track records.
    * Read from file, transform the data and process into sorted lists
    * Display top three fastest times for each athlete
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
def get_athlete_data(filename):
    """ (file) -> list
    Takes <filename>, the file with the athletes' track records.
    Processes each file, creating a list for each athlete’s data.
    Returns the list, otherwise, an error msg and None
    """
    try:
        with open(filename) as file_obj:    # Open the file
            file_data = file_obj.readline() # read the data
        return file_data.strip().split(',') # format the data & return to calling code
    except IOError as ioerr:
        print('File Error...', ioerr)
        return None

if __name__ == '__main__':
    # Init & populate
    sarah = get_athlete_data('text/sarah2.txt') # Gross Info
    sarah_data = {}                             # 
    sarah_data['Name'] = sarah.pop(0)           # Pop & assign name
    sarah_data['DOB'] = sarah.pop(0)            # Pop & assign DOB
    sarah_data['Times'] = sarah                 # Assign times

    # Display Athlete Info
    print('Name : {0}   DOB : {1}'.format(sarah_data['Name'], sarah_data['DOB']))
    print('Top 3 fastest times are : {0}'.format(
        sorted(set([sanitize(each_time) for each_time in sarah_data['Times']]))[0:3]))

    # TODO: Move processing to get_athlete_data() - Return dictionary
    # Init dict and populate 