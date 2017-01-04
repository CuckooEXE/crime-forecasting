########################################################################################################################
#                                                  IMPORT LIBRARIES
#
#   pyproj - coordinate library for python
#   glob - detect files inside a directory for parsing
#   csv - edit CSV files
########################################################################################################################
from pyproj import Proj, transform
import glob
import csv

########################################################################################################################
#                                                  GLOBAL VARIABLES
#
#   inProj - the crazy coordinate system they use
#   outProj - lat/lon coordinate system
########################################################################################################################
inProj = Proj(init='epsg:3857')
outProj = Proj(init='epsg:4326')


########################################################################################################################
#                                                  FUNCTION: MAIN
#   Drives the program (old habits die hard)
########################################################################################################################
def main():
    #Create the final document
    f = open('lat-lon', 'w')

    # Get the files in the CSV folder
    csvFiles = glob.glob("csv/*.csv")

    # Loop through them and make a super CSV
    for filename in csvFiles:
        csvFile = open(filename, 'rt')
        reader = csv.reader(csvFile)
        for row in reader:
            if "x_coordinate" not in row:
                x,y=transform(inProj,outProj,float(row[5]),float(row[6]))
                f.write(row[0].strip(' ') + '\t')
                f.write(row[1].strip(' ') + '\t')
                f.write(row[2].strip(' ') + '\t')
                f.write(row[3].strip(' ') + '\t')
                f.write(row[4].strip(' ') + '\t')
                f.write(str(x)+ '\t')
                f.write(str(y) + '\t')
                f.write(row[7].strip(' '))

    f.close()
main()