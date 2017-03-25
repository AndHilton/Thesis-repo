### ------------------------------------------------------------
"""
A module containing utilities for building faces and tetrahedron
for the grammar

Author : AHilton
"""
### ------------------------------------------------------------

import numpy as np
from grammar import Face
import math
import itertools
from grammar.calculations import isVert_inList
import random

defaultPoints = [[0,0,0],
                 [1,0,0],
                 [1/2,math.sqrt(3)/2,0],
                 [1/2,1/(2*math.sqrt(3)),math.sqrt(2/3)]]
defaultLabels = ["A","B","C","D"]

###
# Returns a list of faces at the "default" location for a tetrahedron
#
# a list of labels (or flat string) to be used in the initial configuration
# can be given
###
def buildDefaultTetra(start):
    if start == "default":
        labels = defaultLabels
    elif "random" in start:
        labels = randomLabels(start[1])
    labels = list(labels)
    vertices = [np.array(v) for v in defaultPoints]
    combos = list(itertools.combinations(vertices,3))
    vertsets = [(base,ext) for base in combos for ext in vertices if not isVert_inList(ext,base)]
    faces = []
    for label,sets in zip(labels,vertsets):
        nextFace = Face(label,sets[0],sets[1])
        faces.append(nextFace)
    return faces
    
###
# returns a list of starting labels chosen randomly from a given pool of labels
###
def randomLabels(pool):
    labels = []
    for i in range(4):
        labels.append(random.choice(pool))
    return labels
