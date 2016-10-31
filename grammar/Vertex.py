### ------------------------------------------------------------
"""
The Vertex class represents the physical vertices of the tetrahedra
that make up the faces and bodies in the system.  They are represented
in 3D space, and therefore have x,y,z components

Author : AHilton

DEPRECATED
"""
### ------------------------------------------------------------

import numpy as np


class Vertex:

    vec = np.zeros(1,3)


    ##
    # Takes the x,y,z coordinates of the point as arguments
    #
    # Default (0,0,0)
    ##
    def __init__ (self, x, y, z):

        self.vec = np.array([x,y,z])


    ##
    # Returns the x-component of the vertex
    ##
    def x(self):
        return self.vec[0]

    ##
    # Returns the y-component of the vertex
    ##
    def y(self):
        return self.vec[1]

    ##
    # Returns the z-component of the vertex
    ##
    def z(self):
        return self.vec[2]

    ##
    # Returns the underlying array, to make adding stuff easier
    ##
    def vector(self):
        return self.vec
