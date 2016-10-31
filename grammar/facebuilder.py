### ------------------------------------------------------------
"""
This module just provides tools to generate faces easily

Author : AHilton
"""
### ------------------------------------------------------------

import numpy as np
from Face import Face
import math
import random as r


###
# builds a face at the "default" base location, with the "default" label
###
def build_default_face():
    label = "A"
    vert1 = np.array([0,0,0])
    vert2 = np.array([1,0,0])
    vert3 = np.array([1/2,math.sqrt(3)/2,0])
    return Face(label,vert1,vert2,vert3)

# ###
# # builds a face at a random point within the given bounds
# ###
# def build_random_face(xmin=-10,xmax=10,ymin=-10,ymax=10,zmin=-10,zmax=10):
#     xPos = r.uniform(xmin,xmax)
#     yPos = r.uniform(ymin,ymax)
#     zPos = r.uniform(zmin,zmax)
#     vert1 = np.array([xPos,yPos,zPos])


    
# ### ------------------------------------------------------------
# ### Helper Functions
# ### ------------------------------------------------------------

# def find_normal_edge(points):
#     searching = False
#     while searching:
#         xPos = r.uniform(xmin,xmax)
#         yPos = r.uniform(ymin,ymax)
#         zPos = r.uniform(zmin,zmax)
#         test = np.array([xPos,yPos,zPos]
