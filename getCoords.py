########################################################################################################################
#                                                  GLOBAL VARIABLES
#
#   coords - list of tuples of coordinates [(x,y), (x,y), ...]
########################################################################################################################
coords = []


########################################################################################################################
#                                                  FUNCTION: COORDS
#   Gets a list of coords, assigns them to a global var (in case script changes in the future) and returns it
########################################################################################################################
def getCoords():
    # Open the file with all the coordinates
    with open('lat-lon', 'r') as file:
        # Tell Python we're going to change a global var
        global coords

        # Loop through and create a list
        for line in file:
            print line
            line = [splits for splits in line.split("\t") if splits is not ""]
            coords.append([line[5],line[6]])

    return coords

getCoords()
# Usage: from getCoords import getCoords