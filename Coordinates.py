########################################################################################################################
#                                                  IMPORT LIBRARIES
#
#   dateutil.parser.parse - Convert the date to python date object
#   random - Get random samples of data
########################################################################################################################
from dateutil.parser import parse
import random

####################################################################################################################
#                                                  Class: Coordinates
#   coordinate driver engine
####################################################################################################################
class Coordinates:
    ####################################################################################################################
    #                                                  GLOBAL VARIABLES
    #   searchColumns [int, int, ...]: indices of columns to search for terms
    #   latlonColumns [int, int]: indices of lat and lon column
    #   latlon [[x,y], [x,y], ...]: List of lat lon
    #   metaData [[], [], [], ...]: List of complete metadata
    #   data [[], [], [], ..]: List of metadata and lat lon data
    ####################################################################################################################
    searchColumns = []
    latlonColumns = []
    latlon = []
    metaData = []
    data = []
    dateColumn = None

    ####################################################################################################################
    #                                                  FUNCTION: init
    #   init function to declare object
    #   Parameters:
    #       - searchColumns [int, int, ...]: indices of columns to search for terms
    #       - latlonColumns [int, int]: indices of lat and lon column
    #       - filename (string): name of file
    ####################################################################################################################
    def __init__(self, filename, dateColumn, searchColumns=[], latlonColumns=[]):
        self.searchColumns = searchColumns
        self.latlonColumns = latlonColumns
        self.dateColumn = dateColumn

        # Open the file with all the coordinates
        with open(filename, 'r') as file:
            # Loop through and create a list
            self.metaData =  [[splits for i,splits in enumerate(line.strip('\n').split("\t")) if splits is not "" and i not in latlonColumns] for line in file]
            file.seek(0,0)
            self.data = [[splits for i,splits in enumerate(line.strip('\n').split("\t")) if splits is not ""] for line in file]
            file.seek(0, 0)
            self.latlon = [[float([splits for splits in line.strip('\n').split("\t") if splits is not ""][latlonColumns[0]]), float([splits for splits in line.strip('\n').split("\t") if splits is not ""][latlonColumns[1]])] for line in file]
            print "Finished building class data"

    ####################################################################################################################
    #                                                  FUNCTION: getSample
    #   get a random sample of data
    #   Parameters:
    #       - count (int): number of samples to return
    ####################################################################################################################
    def getSample(self, count):
        return random.sample(self.data, count)

    ####################################################################################################################
    #                                                  FUNCTION: extractLatLon
    #   Extract latlon from data
    #   Parameters:
    #       - data (self.data): full list of data
    ####################################################################################################################
    def extractLatLon(self, data):
        return [[line[self.latlonColumns[0]], line[self.latlonColumns[1]]] for line in data]

    ####################################################################################################################
    #                                                  FUNCTION: extractMetadata
    #   Extract metadata from data
    #   Parameters:
    #       - data (self.data): full list of data
    ####################################################################################################################
    def extractMetadata(self, data):
        return [[word for i, word in enumerate(line) if i in self.searchColumns] for line in data]

    ########################################################################################################################
    #                                                  FUNCTION: getSet
    #   Returns data from user specified categories
    #   Parameters:
    #       wordList ([string, string, ...]) - Query words
    ########################################################################################################################
    def getSet(self, wordList):
        returnSet = []
        # Loop through and create a list
        for line in self.data:
            possibleWords = [line[x] for x in self.searchColumns]
            if len(set(possibleWords) & set(wordList)) > 0:
                returnSet.append(line)
        return returnSet

    ########################################################################################################################
    #                                                  FUNCTION: filterDate
    #   Returns data from user specified categories
    #   Parameters:
    #       toDate - last Date to filter
    #       fromDate - first Date to filter
    ########################################################################################################################
    def filterDate(self, fromDate, toDate):
        returnSet = []
        # Loop through and create a list
        for line in self.data:
            if parse(line[self.dateColumn]) >= parse(fromDate) and parse(line[self.dateColumn]) <= parse(toDate):
                returnSet.append(line)
        return returnSet



"""
Sample row with headers and indices:
0               1               2                   3                         4           5                 6                7
CATEGORY	    CALL GROUPS	    final_case_type	    CASE DESC	              occ_date    x_coordinate      y_coordinate	 census_tract
STREET CRIMES	DISORDER	    DISTP	            DISTURBANCE - PRIORITY    3/5/12	  -122.723637161    45.4477969437    6404

"""

"""
Unique fields by index:
['STREET CRIMES', 'OTHER', 'MOTOR VEHICLE THEFT', 'BURGLARY']
['DISORDER', 'PERSON CRIME', 'SUSPICIOUS', 'NON CRIMINAL/ADMIN', 'PROPERTY CRIME', 'TRAFFIC']
['DISTP', 'DISTW', 'VICE', 'ASSLTP', 'ASSLTW', 'ROBP', 'ROBW', 'SHOOTW', 'SHOTS', 'STABW', 'THRETP', 'THRETW', 'GANG', 'AREACK', 'PREMCK', 'SUSP', 'SUSPP', 'SUSPW', 'ANIML', 'ANIMLP', 'BOMBTH', 'CHEMTH', 'DIST', 'ESCAPE', 'FWB', 'FWH', 'FWI', 'FWN', 'NOISE', 'CHEM', 'PARK', 'PARTY', 'POLINV', 'SCHL', 'SCHLP', 'THRET', 'TMET', 'TMETP', 'TRASH', 'TRASHP', 'UNWNT', 'TMETW', 'UNWNTP', 'UNWNTW', 'W26', 'ASSIST', '77', 'CIVIL', 'EVICT', 'FOLLOW', 'MSG', 'FLAG', 'PROP', 'RED', 'RIVPOL', 'SEIZE', 'SERVE', 'STNDBY', 'TRANS', 'WARR', 'WARRC', 'WELCK', 'SUBSTP', 'WELCKP', 'ASSLT', 'DEVICE', 'ROB', 'SHOOT', 'STAB', 'BURG', 'FRAUD', 'FRAUDP', 'THEFT', 'IDENT', 'THEFTC', 'THEFTP', 'VAND', 'VANDP', 'VEHST', 'ACCHR', 'ACCHRP', 'ACCINJ', 'ACCNON', 'ACCUNK', 'DUII', 'HAZARD', 'TRASTP', 'WRONG', 'FPURS', 'TPURS', 'VEHREC', 'VEHSTP', 'PROWLP', 'BURGP', 'SCHLW', 'RSTLN', 'ZERO', 'GREAT', 'SCHLET', 'HOSTGE']
['DISTURBANCE - PRIORITY', 'DISTURBANCE - WITH WEAPON *H', 'VICE-DRUGS, LIQUOR, PROSTITUTION, GAMBLING', 'ASSAULT - PRIORITY', 'ASSAULT - WITH WEAPON *H', 'ROBBERY - PRIORITY *H', 'ROBBERY - WITH WEAPON *H', 'SHOOTING - WITH WEAPON *H', 'SHOTS FIRED', 'STABBING - WITH WEAPON *H', 'THREAT - PRIORITY', 'THREAT - WITH WEAPON *H', 'GANG RELATED', 'AREA CHECK', 'PREMISE CHECK', 'SUSPICIOUS SUBJ, VEH, OR CIRCUMSTANCE', 'SUSPICIOUS - PRIORITY', 'SUSPICIOUS - WITH WEAPON *H', 'ANIMAL PROBLEM', 'ANIMAL PROBLEM - PRIORITY', 'BOMB - THREAT (33B)', 'CHEMICAL OR BIOLOGICAL THREAT (33CTH)', 'DISTURBANCE - COLD', 'ESCAPE FROM CUSTODY', 'FIREWORKS - NOISE (BROADCAST ONLY)', 'FIREWORKS - HAZARD', 'FIREWORKS - ILLEGAL', 'FIREWORKS - NOISE (MDC DISPATCH)', 'NOISE DISTURBANCE', 'CHEMICAL OR BIOLOGICAL (33C)', 'PARKING PROBLEM', 'PARTY DISTURBANCE', 'BOMB OR CHEM POLICE INVESTIGATION (33B/33C)', 'SCHOOL INCIDENT - COLD', 'SCHOOL INCIDENT - PRIORITY', 'THREAT - COLD', 'TRIMET INCIDENT - COLD', 'TRIMET INCIDENT - PRIORITY', 'ILLEGAL DUMPING - COLD', 'ILLEGAL DUMPING - PRIORITY', 'UNWANTED PERSON', 'TRIMET INCIDENT - WITH WEAPON *H', 'UNWANTED PERSON - PRIORITY', 'UNWANTED PERSON - WITH WEAPON *H', 'DETOX TRANSPORT', 'ASSIST - CITIZEN OR AGENCY', 'SUBJECT STOP - SDC', 'CIVIL - CIVIL PROBLEM', 'CIVIL - EVICTION', 'FOLLOW-UP', 'DELIVER MESSAGE', 'FLAGDOWN', 'PROPERTY LOST, FOUND, RECOVERED', 'ASSISTANCE - FIRE / EMS NEED POLICE *H', 'RIVER - MARINE INCIDENT', 'CIVIL - PROPERTY SEIZURE', 'CIVIL - SERVE PAPERS', 'CIVIL - STANDBY', 'TRANSPORT', 'WARRANT', 'WARRANT - WALK-IN / COUNTER', 'WELFARE CHECK - COLD', 'PERSON CONTACT (86)', 'WELFARE CHECK - PRIORITY', 'ASSAULT - COLD', 'BOMB - DEVICE DISCOVERED (33B) *H', 'ROBBERY - COLD', 'SHOOTING - COLD', 'STABBING - COLD', 'BURGLARY - COLD', 'FRAUD - COLD', 'FRAUD - PRIORITY', 'THEFT - COLD', 'IDENTITY THEFT', 'THEFT - SUBJECT IN CUSTODY', 'THEFT - PRIORITY', 'VANDALISM - COLD', 'VANDALISM - PRIORITY', 'VEHICLE STOLEN - COLD', 'ACCIDENT - HIT AND RUN - COLD', 'ACCIDENT - HIT & RUN - PRIORITY', 'ACCIDENT - INJURY', 'ACCIDENT - NON INJURY', 'ACCIDENT - UNKNOWN INJURY', 'DRIVING UNDER INFLUENCE', 'HAZARD - HAZARDOUS CONDITION', 'TRAFFIC STOP', 'HAZARD - WRONG-WAY DRIVER *H', 'FOOT PURSUIT *H', 'TRAFFIC PURSUIT *H', 'VEHICLE RECOVERED', 'VEHICLE STOLEN - PRIORITY', 'PROWLER', 'BURGLARY - PRIORITY *H', 'SCHOOL INCIDENT - WITH WEAPON *H', 'ROLLING STOLEN *H', 'ASSISTANCE - RESPONDER EMERGENCY *H', 'GREAT - SRO INITIATED ACTIVITY', 'SCHOOL EVENTS', 'HOSTAGE SITUATION *H']
"""