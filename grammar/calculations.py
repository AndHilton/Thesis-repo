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
    return abs(np.linalg.norm(A-B)) < THRESHOLD
