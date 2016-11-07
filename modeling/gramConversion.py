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
