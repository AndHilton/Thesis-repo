### ------------------------------------------------------------
"""
The Vertex class represents the physical vertices of the tetrahedra
that make up the faces and bodies in the system.  They are represented
in 3D space, and therefore have x,y,z components

Author : AHilton
"""
### ------------------------------------------------------------

import numpy as np


class Vertex:

    vec = np.zeros(1,3)


    def __init__ (self, x, y, z):

        self.vec = np.array([x,y,z])
