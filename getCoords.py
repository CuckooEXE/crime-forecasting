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
        for line in file:
            line = [splits for splits in line.split("\t") if splits is not ""]
            coords.append([float(line[5]),float(line[6])])
    return sorted(coords, key=lambda x: parse(x[4]), reverse=reversed)

########################################################################################################################
#                                                  FUNCTION: getUnique
#   Returns a list of unique fields for fields 0-3
########################################################################################################################
def getUnique():
    with open('lat-lon', 'r') as file:
        fields = [[],[],[],[]]
        for line in file:
            line = [splits for splits in line.split("\t") if splits is not ""]
            if line[0] not in fields[0]:
                fields[0].append(line[0])
            if line[1] not in fields[1]:
                fields[1].append(line[1])
            if line[2] not in fields[2]:
                fields[2].append(line[2])
            if line[3] not in fields[3]:
                fields[3].append(line[3])
    return fields

print getUnique()
# Usage: from getCoords import getCoords OR import getAll  ... foo = getCoords.getAll()

"""
Sample row with headers and indices:
0               1               2                   3                         4           5                 6                7
CATEGORY	    CALL GROUPS	    final_case_type	    CASE DESC	              occ_date    x_coordinate      y_coordinate	 census_tract
STREET CRIMES	DISORDER	    DISTP	            DISTURBANCE - PRIORITY    3/5/12	  -122.723637161    45.4477969437    6404

"""

"""
Unique fields by index:
[['STREET CRIMES', 'OTHER', 'MOTOR VEHICLE THEFT', 'BURGLARY']
['DISORDER', 'PERSON CRIME', 'SUSPICIOUS', 'NON CRIMINAL/ADMIN', 'PROPERTY CRIME', 'TRAFFIC']
['DISTP', 'DISTW', 'VICE', 'ASSLTP', 'ASSLTW', 'ROBP', 'ROBW', 'SHOOTW', 'SHOTS', 'STABW', 'THRETP', 'THRETW', 'GANG', 'AREACK', 'PREMCK', 'SUSP', 'SUSPP', 'SUSPW', 'ANIML', 'ANIMLP', 'BOMBTH', 'CHEMTH', 'DIST', 'ESCAPE', 'FWB', 'FWH', 'FWI', 'FWN', 'NOISE', 'CHEM', 'PARK', 'PARTY', 'POLINV', 'SCHL', 'SCHLP', 'THRET', 'TMET', 'TMETP', 'TRASH', 'TRASHP', 'UNWNT', 'TMETW', 'UNWNTP', 'UNWNTW', 'W26', 'ASSIST', '77', 'CIVIL', 'EVICT', 'FOLLOW', 'MSG', 'FLAG', 'PROP', 'RED', 'RIVPOL', 'SEIZE', 'SERVE', 'STNDBY', 'TRANS', 'WARR', 'WARRC', 'WELCK', 'SUBSTP', 'WELCKP', 'ASSLT', 'DEVICE', 'ROB', 'SHOOT', 'STAB', 'BURG', 'FRAUD', 'FRAUDP', 'THEFT', 'IDENT', 'THEFTC', 'THEFTP', 'VAND', 'VANDP', 'VEHST', 'ACCHR', 'ACCHRP', 'ACCINJ', 'ACCNON', 'ACCUNK', 'DUII', 'HAZARD', 'TRASTP', 'WRONG', 'FPURS', 'TPURS', 'VEHREC', 'VEHSTP', 'PROWLP', 'BURGP', 'SCHLW', 'RSTLN', 'ZERO', 'GREAT', 'SCHLET', 'HOSTGE']
['DISTURBANCE - PRIORITY', 'DISTURBANCE - WITH WEAPON *H', 'VICE-DRUGS, LIQUOR, PROSTITUTION, GAMBLING', 'ASSAULT - PRIORITY', 'ASSAULT - WITH WEAPON *H', 'ROBBERY - PRIORITY *H', 'ROBBERY - WITH WEAPON *H', 'SHOOTING - WITH WEAPON *H', 'SHOTS FIRED', 'STABBING - WITH WEAPON *H', 'THREAT - PRIORITY', 'THREAT - WITH WEAPON *H', 'GANG RELATED', 'AREA CHECK', 'PREMISE CHECK', 'SUSPICIOUS SUBJ, VEH, OR CIRCUMSTANCE', 'SUSPICIOUS - PRIORITY', 'SUSPICIOUS - WITH WEAPON *H', 'ANIMAL PROBLEM', 'ANIMAL PROBLEM - PRIORITY', 'BOMB - THREAT (33B)', 'CHEMICAL OR BIOLOGICAL THREAT (33CTH)', 'DISTURBANCE - COLD', 'ESCAPE FROM CUSTODY', 'FIREWORKS - NOISE (BROADCAST ONLY)', 'FIREWORKS - HAZARD', 'FIREWORKS - ILLEGAL', 'FIREWORKS - NOISE (MDC DISPATCH)', 'NOISE DISTURBANCE', 'CHEMICAL OR BIOLOGICAL (33C)', 'PARKING PROBLEM', 'PARTY DISTURBANCE', 'BOMB OR CHEM POLICE INVESTIGATION (33B/33C)', 'SCHOOL INCIDENT - COLD', 'SCHOOL INCIDENT - PRIORITY', 'THREAT - COLD', 'TRIMET INCIDENT - COLD', 'TRIMET INCIDENT - PRIORITY', 'ILLEGAL DUMPING - COLD', 'ILLEGAL DUMPING - PRIORITY', 'UNWANTED PERSON', 'TRIMET INCIDENT - WITH WEAPON *H', 'UNWANTED PERSON - PRIORITY', 'UNWANTED PERSON - WITH WEAPON *H', 'DETOX TRANSPORT', 'ASSIST - CITIZEN OR AGENCY', 'SUBJECT STOP - SDC', 'CIVIL - CIVIL PROBLEM', 'CIVIL - EVICTION', 'FOLLOW-UP', 'DELIVER MESSAGE', 'FLAGDOWN', 'PROPERTY LOST, FOUND, RECOVERED', 'ASSISTANCE - FIRE / EMS NEED POLICE *H', 'RIVER - MARINE INCIDENT', 'CIVIL - PROPERTY SEIZURE', 'CIVIL - SERVE PAPERS', 'CIVIL - STANDBY', 'TRANSPORT', 'WARRANT', 'WARRANT - WALK-IN / COUNTER', 'WELFARE CHECK - COLD', 'PERSON CONTACT (86)', 'WELFARE CHECK - PRIORITY', 'ASSAULT - COLD', 'BOMB - DEVICE DISCOVERED (33B) *H', 'ROBBERY - COLD', 'SHOOTING - COLD', 'STABBING - COLD', 'BURGLARY - COLD', 'FRAUD - COLD', 'FRAUD - PRIORITY', 'THEFT - COLD', 'IDENTITY THEFT', 'THEFT - SUBJECT IN CUSTODY', 'THEFT - PRIORITY', 'VANDALISM - COLD', 'VANDALISM - PRIORITY', 'VEHICLE STOLEN - COLD', 'ACCIDENT - HIT AND RUN - COLD', 'ACCIDENT - HIT & RUN - PRIORITY', 'ACCIDENT - INJURY', 'ACCIDENT - NON INJURY', 'ACCIDENT - UNKNOWN INJURY', 'DRIVING UNDER INFLUENCE', 'HAZARD - HAZARDOUS CONDITION', 'TRAFFIC STOP', 'HAZARD - WRONG-WAY DRIVER *H', 'FOOT PURSUIT *H', 'TRAFFIC PURSUIT *H', 'VEHICLE RECOVERED', 'VEHICLE STOLEN - PRIORITY', 'PROWLER', 'BURGLARY - PRIORITY *H', 'SCHOOL INCIDENT - WITH WEAPON *H', 'ROLLING STOLEN *H', 'ASSISTANCE - RESPONDER EMERGENCY *H', 'GREAT - SRO INITIATED ACTIVITY', 'SCHOOL EVENTS', 'HOSTAGE SITUATION *H']
"""