#!/usr/bin/env python3
""" Track Coach Data 
A play on files and working the data files, 
text files holding athletes track records.
    * Read from file, transform the data and process into sorted lists
    * Display top three fastest times for each athlete
"""
# TODO: Create and define OO class to associate code with the data it operates on


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
def get_athlete_top3(filename):
    """ (file) -> dict
    Takes <filename>, the file with the athletes' track records.
    Processes each file, creating a dictionary for each athlete’s data.
    
    Returns the dictionary populated with athletes name, DOB and Top3 fastest
    recorded times, otherwise, an error msg and None
    """
    try:
        with open(filename) as file_obj:    # Open the file
            file_data = file_obj.readline() # read the data

            temp_list = file_data.strip().split(',') # hold data before populating dict
            # Populate & return dict
            return ({'Name': temp_list.pop(0),  # Pop & assign name
                    'DOB': temp_list.pop(0),    # Pop & assign DOB
                    # Sort and Assign three best recored times
                    'Times': sorted(set([sanitize(t) for t in temp_list]))[0:3]})
    except IOError as ioerr:
        print('File Error...', ioerr)
        return None

if __name__ == '__main__':
    # Init
    sarah = get_athlete_top3('text/sarah2.txt') # Gross Info
    james = get_athlete_top3('text/james2.txt') # Gross Info
    mikey = get_athlete_top3('text/mikey2.txt') # Gross Info
    julie = get_athlete_top3('text/julie2.txt') # Gross Info
   
    # Display Athlete Info
    for record in (sarah, james, mikey, julie):
        print(format(' ATHLETE INFO ', '*^60'))
        print('Name : {0}   DOB : {1}'.format(record['Name'], record['DOB']))
        print('Top 3 fastest times are : {0}'.format(record['Times']))
        print()
