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
#                                                  FUNCTION: main
#   Drives the program (old habits die hard)
########################################################################################################################
def main():
    #Create the final document
    allData = open('lat-lono', 'w')
    sampleData = open('sampleo', 'w')

    # Get the files in the CSV folder
    csvFiles = glob.glob("csv/*.csv")

    # Loop through them and make a super CSV
    for filename in csvFiles:
        csvFile = open(filename, 'rt')
        reader = csv.reader(csvFile)
        for row in reader:
            if "x_coordinate" not in row:
                inProj = Proj(init='esri:102726')
                outProj = Proj(init='epsg:4236')
                x,y=transform(inProj,outProj,float(row[5]),float(row[6]))
                print x, y
                allData.write(row[0].strip(' ') + '\t')
                allData.write(row[1].strip(' ') + '\t')
                allData.write(row[2].strip(' ') + '\t')
                allData.write(row[3].strip(' ') + '\t')
                allData.write(row[4].strip(' ') + '\t')
                allData.write(str(x)+ '\t')
                allData.write(str(y) + '\t')
                allData.write(row[7].strip(' '))
                allData.write('\n')

    sampleData.write(allData[:50])
    allData.close()
    sampleData.close()
main()