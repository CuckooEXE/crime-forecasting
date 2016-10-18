# Import known Python modules. Used to install modules, check if they're installed, and work with finding files
import imp
import os
import glob

# If the necessary modules aren't installed, install them!
try:
    imp.find_module('csv')
except ImportError:
	os.system("pip install csv")

try:
    imp.find_module('pyproj')
except ImportError:
	os.system("pip install pyproj")

# Now that we know the modules are in, import them
import csv
from pyproj import Proj, transform

csvFiles = glob.glob("csv/*.csv")

for filename in csvFiles:
	csvFile = open(filename, 'rt')
	reader = csv.reader(csvFile)
	newCsv = []
	for row in reader:
		if "x_coordinate" not in row:
			tempRow = row
			inProj = Proj(init='epsg:3857')
			outProj = Proj(init='epsg:4326')
			x1,y1 = float(row[5]),float(row[6])
			tempRow[5],tempRow[6] = transform(inProj,outProj,x1,y1)

			newCsv.append(tempRow)

	csvFile.close()

	csvFile = open(filename, 'wb')
	writer = csv.writer(csvFile)
	writer.writerows(newCsv)

	csvFile.close()
