### ------------------------------------------------------------
"""
Using the numpy arrays to implement the vertices of Faces, but
overriding the comparison to account for errors in floating point
rounding
"""
### ------------------------------------------------------------

import numpy as np


class Vertex:

    THRESHOLD = 10^(-12)
    vec = None
    

    def __init__(self,x,y,z):
        self.vec = np.array([x,y,z])

    def __str__(self):
        return "Vertex located at ({},{},{})".format(self.x(),self.y(),self.z())

    ## ------------------------- ##
    ## Overloading Operators     ##
    ## ------------------------- ##

    def __add__(self,other):
        return self.vec + other.vec
    

    ## ------------------------- ##
    ## ------------------------- ##

    def x(self):
        return self.vec[0]

    def y(self):
        return self.vec[1]

    def z(self):
        return self.vec[2]
