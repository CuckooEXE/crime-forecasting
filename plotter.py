########################################################################################################################
#                                                  IMPORT LIBRARIES
#
#   basemap - rendering the map
#   matplotlib:
#               - plt: Plot the map
#               - Basemap: Map drawing utility
#   getCoords - get the coordinates from the lat-lon file
#   time - sleep between point plots (animation purposes)
#   os - detect if the map is displayed (async animation purposes)
########################################################################################################################
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from getCoords
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
coords = getCoords.getAll()

########################################################################################################################
#                                                  FUNCTION: plotPoints
#   Plot the crime data points onto the map
########################################################################################################################
def plotPoints():
    for tuple in coords:
        portland.plot(tuple[0], tuple[1], 'bo', markersize=7, latlon=True)



########################################################################################################################
#                                                  FUNCTION: main
#   Drives the program (old habits die hard)
########################################################################################################################
def main():
    # Draw ArcGIS layer
    portland.arcgisimage(service='World_Street_Map', xpixels = 150000)

    # Draw the points on the map
    plotPoints()

    # Render the map
    plt.show()

main()


# Portland Bounded Box: westlimit=-122.836761; southlimit=45.433154; eastlimit=-122.469406; northlimit=45.655088