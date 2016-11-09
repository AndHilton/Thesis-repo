### ------------------------------------------------------------
"""
This module provides functions that convert the grammar data into
data that is usable by the modeling system
"""
### ------------------------------------------------------------

import grammar as gram
import modeling
import numpy


###
# takes a Face object in as an argument, and converts its vertex
# data into a list of tuples that can then be used to create meshes
###
def face_toVertList(gramFace):
    vertList = [tuple(arr.tolist()) for arr in gramFace.getVertices()]
    return vertList


###
# takes in a GrammarRun object, and adds geometry to the current project
# and scene to represent the current state of the GrammarRun
###
def modelGrammar(gramRun):
    faceList = gramRun.getFaces()
    for idx in range(len(faceList)):
        vertList = face_toVertList(faceList[idx])
        modeling.add_geometry.add_tetraFace(vertList,"Face{}".format(idx))
    
