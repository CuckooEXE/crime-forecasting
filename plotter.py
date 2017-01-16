########################################################################################################################
#                                                  IMPORT LIBRARIES
#
#   basemap - rendering the map
#   matplotlib:
#               - plt: Plot the map
#               - Basemap: Map drawing utility
#   Coordinates - Custom coordinate engine
#   time - sleep between point plots (animation purposes)
#   os - detect if the map is displayed (async animation purposes)
########################################################################################################################
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import Coordinates
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

coords = Coordinates.Coordinates('lat-lon', 4, searchColumns=[0,1,2,3], latlonColumns=[5,6])
testCoords = Coordinates.Coordinates('lat-lon', 4, searchColumns=[0,1,2,3], latlonColumns=[5,6], fullData=coords.getSet(["ASSAULT - WITH WEAPON *H"]))

########################################################################################################################
#                                                  FUNCTION: plotPoints
#   Plot the crime data points onto the map
########################################################################################################################
def plotPoints(coords):
    for tuple in coords:
        print tuple
        portland.plot(float(tuple[0]), float(tuple[1]), 'bo', markersize=7, latlon=True)



########################################################################################################################
#                                                  FUNCTION: main
#   Drives the program (old habits die hard)
########################################################################################################################
def main():
    # Draw ArcGIS layer
    portland.arcgisimage(service='World_Street_Map', xpixels = 150000)

    # Draw the points on the map
    plotPoints(testCoords.extractLatLon(testCoords.data))

    # Render the map
    plt.show()

main()


# Portland Bounded Box: westlimit=-122.836761; southlimit=45.433154; eastlimit=-122.469406; northlimit=45.655088