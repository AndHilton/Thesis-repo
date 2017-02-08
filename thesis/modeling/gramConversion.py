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
# takes a GrammarRun object, and writes its current configuration
# to an STL file
###
def outputSTL(gramRun,filename):
    convert_facelist(gramRun.getFaces(),filename)

###
# Takes a list of faces writes them to an stl file
###
def convert_facelist(facelist,filename):
    print("Writing output to {}".format(filename))
    f = open(filename,"w")
    f.write("solid foo\n")
    for face in facelist:
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
