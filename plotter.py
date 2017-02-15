########################################################################################################################
#                                                  IMPORT LIBRARIES
#
#   basemap - rendering the map
#   matplotlib:
#               - plt: Plot the map
#               - Basemap: Map drawing utility
#   Coordinates - Custom coordinate engine
#   LOF - Local outlier factor calculator
#   time - sleep between point plots (animation purposes)
#   os - detect if the map is displayed (async animation purposes)
########################################################################################################################
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import Coordinates
import lof
import time
import os

########################################################################################################################
#                                                  GLOBAL VARIABLES
#
#   portland - portland map into the area we want (Portland, OR)
#               Resolutions are crude (c), low (l), intermediate (i), high (h), or full (f)
#   coords - list of tuples of coordinates [(x,y), (x,y), ...]
########################################################################################################################
portland = Basemap(projection='merc', resolution='c', epsg=4326, lon_0=-122.64, lat_0=45.54,
                  area_thresh=1000.0, llcrnrlon=-122.83, llcrnrlat=45.43, urcrnrlon=-122.46, urcrnrlat=45.65)

coords = Coordinates.Coordinates(filename='lat-lon', dateColumn=4, searchColumns=[0,1,2,3], latlonColumns=[5,6], fullData=None)

########################################################################################################################
#                                                  FUNCTION: plotPoints
#   Plot the crime data points onto the map
########################################################################################################################
def plotPoints(coords):
    LOF = lof.outliers(5, coords)

    '''
    for coord in coords:
        if lof.local_outlier_factor(5, coord) > 1:
            portland.plot(float(coord[0]), float(coord[1]), 'ro', markersize=7, latlon=True)
        else:
            portland.plot(float(coord[0]), float(coord[1]), 'bo', markersize=7, latlon=True)
    '''
    print LOF
    '''
    for tuple in coords:
        portland.plot(float(tuple[0]), float(tuple[1]), 'bo', markersize=7, latlon=True)
    for outlier in LOF:
        portland.plot(float(outlier['instance'][0]), float(outlier['instance'][1]), 'ro', markersize=7, latlon=True)
    '''


########################################################################################################################
#                                                  FUNCTION: main
#   Drives the program (old habits die hard)
########################################################################################################################
def main():
    sample = coords.getSet(["ASSLTP"], coords.data)
    sample12 = coords.extractLatLon(coords.filterDate("1/1/12", "12/31/12", sample))[:50]
    #sample13 = coords.extractLatLon(coords.filterDate("1/1/13", "12/31/13", sample))
    #sample14 = coords.extractLatLon(coords.filterDate("1/1/14", "12/31/14", sample))
    #sample15 = coords.extractLatLon(coords.filterDate("1/1/15", "12/31/15", sample))

    # Draw the points on the map
    plotPoints(sample12)
    print len(sample12)

    # Draw ArcGIS layer
    portland.arcgisimage(service='World_Street_Map', xpixels = 150000)

    # Render the map
    plt.show()

main()


# Portland Bounded Box: westlimit=-122.836761; southlimit=45.433154; eastlimit=-122.469406; northlimit=45.655088