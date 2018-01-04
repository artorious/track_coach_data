#!/usr/bin/env python3
""" Track Coach Data 
A play on files and working the data files, 
text files holding athletes track records.
    * Read from file, transform the data and process into sorted lists
    * Display top three fastest times for each athlete
"""

class AthleteRecords:
    """ 
    Class routines process Athelete Track information 
    """
    def __init__(self, a_name, a_dob=0, a_times=[]):
        """Initialize class attributes"""
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3_records(self):
        """ Return Athelete's 3 Best recorded times """
        return sorted(set([sanitize(t) for t in self.times]))[0:3]
    
    def avg_record_time(self):
        """ Return Athelete's Average recorded time """
        summed_time = 0
        for time_rec in self.times:
            try:
                summed_time += float(sanitize(time_rec))
            except Exception as err:
                return err
        return summed_time / len(self.times) 

def get_athlete_data(filename):# Process each file
    """ (file) -> Athlete object instance
    Takes <filename>, the file with the athletes' track records.
    Processes each file, creating and returning an Athlete class object 
    for each athlete’s data.
    """
    try:
        with open(filename) as file_obj:    # Open the file
            file_data = file_obj.readline() # read the data
            temp_list = file_data.strip().split(',') # hold gross data in list 
            return AthleteRecords(temp_list.pop(0), temp_list.pop(0), temp_list)
    except IOError as ioerr:
        print('File Error...', ioerr)
        return None

def sanitize(time_string): # Fix non-uniformity in the athletes data to enable sorting
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


if __name__ == '__main__':
    # Init Athlete object instaces
    sarah = get_athlete_data('text/sarah2.txt') # Gross Info
    james = get_athlete_data('text/james2.txt') # Gross Info
    mikey = get_athlete_data('text/mikey2.txt') # Gross Info
    julie = get_athlete_data('text/julie2.txt') # Gross Info
   
    # Display Athlete Info
    for record in (sarah, james, mikey, julie):
        print(format(' ATHLETE INFO ', '*^60'))
        print('Name : {0}   DOB : {1}'.format(record.name, record.dob))
        print('Top 3 fastest times are : {0}'.format(record.top3_records()))
        print('Average Time: {0:.2f}'.format(record.avg_record_time()))
        print(record.times)
        print()
