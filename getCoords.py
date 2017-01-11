########################################################################################################################
#                                                  IMPORT LIBRARIES
#
#   dateutil.parser.parse - Convert the date to python date object
#   operator.itemgetter - Sort a list of list using an index from the inner list (used for sorting by dates)
########################################################################################################################
from dateutil.parser import parse

########################################################################################################################
#                                                  GLOBAL VARIABLES
#
########################################################################################################################


########################################################################################################################
#                                                  FUNCTION: getAll
#   Gets a list of coords and returns it
########################################################################################################################
def getAll():
    # Open the file with all the coordinates
    with open('lat-lon', 'r') as file:
        coords = []
        # Loop through and create a list
        for line in file:
            line = [splits for splits in line.split("\t") if splits is not ""]
            coords.append([float(line[5]),float(line[6])])
    return coords

########################################################################################################################
#                                                  FUNCTION: getSample
#   Returns a list of only 50 coords (for dev purposes)
########################################################################################################################
def getSample():
    with open('lat-lon', 'r') as file:
        coords = []
        # Loop through and create a list
        for i, line in enumerate(file):
            print line
            if i == 51:
                break
            else:
                line = [splits for splits in line.split("\t") if splits is not ""]
                coords.append([float(line[5]),float(line[6])])
    return coords

########################################################################################################################
#                                                  FUNCTION: getSample
#   Returns a list of coords sorted by their date
#   Parameters:
#       reversed (bool) - Reverse the list of dates
########################################################################################################################
def sortDate(reversed):
    with open('lat-lon', 'r') as file:
        coords = []
        # Loop through and create a list
        for i, line in enumerate(file):
            print line
            if i == 51:
                break
            else:
                line = [splits for splits in line.split("\t") if splits is not ""]
                coords.append([float(line[5]),float(line[6])])
    return sorted(coords, key=lambda x: parse(x[4]), reverse=reversed)

# Usage: from getCoords import getCoords OR import getAll  ... foo = getCoords.getAll()

"""Sample row with headers and indices:
0               1               2                   3                         4           5                 6                7
CATEGORY	    CALL GROUPS	    final_case_type	    CASE DESC	              occ_date    x_coordinate      y_coordinate	 census_tract
STREET CRIMES	DISORDER	    DISTP	            DISTURBANCE - PRIORITY    3/5/12	  -122.723637161    45.4477969437    6404

"""

