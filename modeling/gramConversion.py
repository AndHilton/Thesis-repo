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
        modeling.add_geometry.add_tetraFace(vertList,"Face")
    


###
# takes a GrammarRun object, and writes its current configuration
# to an STL file
###
def outputSTL(gramRun,filename):
    print("Writing grammar to {}".format(filename))
    f = open(filename,"w")
    f.write("solid foo\n")
    for face in gramRun.getFaces():
        f.write(face_toSTL(face))
    f.write("endsolid foo")
    f.close

###
# takes a grammar Face and returns a string conversion to stl
###
def face_toSTL(face):
    retstr = ""
    retstr += "facet normal 0 0 0\n"
    retstr += "outer loop\n"
    for vert in face.getVertices():
        retstr += "vertex {} {} {}\n".format(vert[0],vert[1],vert[2])
    retstr += "endloop\n"
    retstr += "endfacet\n"
    return retstr
