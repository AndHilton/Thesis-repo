### ------------------------------------------------------------
"""
<<<<<<< HEAD
This module just provides tools to generate faces easily
=======
A module containing utilities for building faces and tetrahedron
for the grammar
>>>>>>> grammarsys

Author : AHilton
"""
### ------------------------------------------------------------

import numpy as np
from grammar import Face
import math
import itertools

defaultPoints = [[0,0,0],
                 [1,0,0],
                 [1/2,math.sqrt(3)/2,0],
                 [1/2,1/(2*math.sqrt(3)),math.sqrt(3/2)]]
defaultLabels = ["A","B","C","D"]

###
# Returns a list of faces at the "default" location for a tetrahedron
#
# a list of labels (or flat string) to be used in the initial configuration
# can be given
###
def buildDefaultTetra(labels=defaultLabels):
    labels = list(labels)
    vertices = [np.array(v) for v in defaultPoints]
    combos = itertools.combinations(vertices,3)
    faces = []
    for label,vertices in zip(labels,combos):
        nextFace = Face(label,vertices[0],vertices[1],vertices[2])
        faces.append(nextFace)
    return faces
    

