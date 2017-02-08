### ------------------------------------------------------------
"""
Just some utility functions used to calculate metrics about
faces and whatnot
"""
### ------------------------------------------------------------

import numpy as np


THRESHOLD = 10**(-12)

###
# calculates if 2 vertices are "equal" based on a default threshold
# returns true if the vertices are within 
###
def vertexEq(A,B):
    return np.linalg.norm(abs(A-B)) < THRESHOLD

###
# goes through a list of vertices and returns the index of the one which is closest
# to the origin
###
def findClosest(vertList):
    origin = np.array([0,0,0])
    distList = [np.linalg.norm(abs(x-origin)) for x in vertList]
    mindex = distList.index(min(distList))
    return mindex


###
# returns true iff the vertex is an element of the given list of vertices
###
def isVert_inList(avert,vertlist):
    found = False
    idx = 0
    while idx < len(vertlist) and not found:
        found = vertexEq(avert,vertlist[idx])
        idx += 1
    return found
