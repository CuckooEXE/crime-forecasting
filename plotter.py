########################################################################################################################
#                                                  IMPORT LIBRARIES
#
#   basemap - rendering the map
#   matplotlib - plotting the points
#   numpy - handling the data
#   math - conversion of coordinates
########################################################################################################################
import matplotlib.pyplot as plt
import matplotlib.cm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import numpy as np
import math

########################################################################################################################
#                                                  GLOBAL VARIABLES
#
#   inProj - the crazy coordinate system they use
########################################################################################################################
#inProj = Proj(init='epsg:3857')

########################################################################################################################
#                                                  FUNCTION: MAIN
#   Drives the program (old habits die hard)
########################################################################################################################
def main():
    #Create the final document
    f = open('lat-lon', 'r')

    fig, ax = plt.subplots(figsize=(10, 10))

    # Cut the map into the area we want (Portland, OR)
    # Resolutions are crude (c), low (l), intermediate (i), high (h), or full (f)
    portland= Basemap(projection='merc', resolution='c', epsg=4326, lon_0=-122.64, lat_0=45.54,
                      area_thresh=1000.0, llcrnrlon=-122.83, llcrnrlat=45.43, urcrnrlon=-122.46, urcrnrlat=45.65)

    portland.drawmapboundary(fill_color='#46bcec')
    portland.drawcoastlines()
    portland.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 150000)
    plt.show()

    f.close()
main()


# Portland Bounded Box: westlimit=-122.836761; southlimit=45.433154; eastlimit=-122.469406; northlimit=45.655088
# Possible map types (called services) for arcgis layer:
'''ESRI_Imagery_World_2D (MapServer)
ESRI_StreetMap_World_2D (MapServer)
I3_Imagery_Prime_World (GlobeServer)
NASA_CloudCover_World (GlobeServer)
NatGeo_World_Map (MapServer)
NGS_Topo_US_2D (MapServer)
Ocean_Basemap (MapServer)
USA_Topo_Maps (MapServer)
World_Imagery (MapServer)
World_Physical_Map (MapServer)
World_Shaded_Relief (MapServer)
World_Street_Map (MapServer)
World_Terrain_Base (MapServer)
World_Topo_Map (MapServer)
'''