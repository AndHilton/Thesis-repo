### ------------------------------------------------------------
"""
A module containing utilities for building faces and tetrahedron
for the grammar

Author : AHilton
"""
### ------------------------------------------------------------

import numpy as np
from Face import Face
import math
import itertools

defaultPoints = [[0,0,0],
                 [1,0,0],
                 [1/2,math.sqrt(3)/2,0],
                 [1/2,1/2*math.sqrt(3),math.sqrt(3/2)]]
defaultLabels = ["A","B","C","D"]

###
# Returns a list of faces at the "default" location for a tetrahedron
###
def buildDefaultTetra():
    vertices = [np.array(v) for v in defaultPoints]
    combos = itertools.combinations(vertices,3)
    faces = []
    for label,vertices in zip(defaultLabels,combos):
        nextFace = Face(label,vertices[0],vertices[1],vertices[2])
        faces.append(nextFace)
    return faces
    
