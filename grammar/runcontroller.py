### ------------------------------------------------------------
"""
a module that provides an interface between the Grammar productions
and the other parts of the system

Author : AHilton
"""
### ------------------------------------------------------------

import numpy as np
from Face import Face
from GrammarRun import GrammarRun as GR
import calculations as calc
import facebuilder as fb


### ------------------------- ###
###     GRAMMAR OPERATIONS    ###
### ------------------------- ###

###
# The function for the relabel operation of the grammar
# takes in a grammar run, the face being operated on, and a list
# containing the new label in as arguments
#
# (these requirements are because the function header has to be
# identical to the header for grow)
#
# returns a tuple containing a list the relabled face, and None
###
def relabel(gramRun,face,paramsList):
    newLabel = paramsList[0]
    face.changeLabel(newLabel)
    return ([face],None)


###
# the function for the grow operation of the grammar
# takes in a grammar run, the face being operated on, and a list
# containing the label for the new faces being produced
#
# returns a tuple containing a list of the new faces, and the new Vertex
###
def grow(gramRun,face,paramsList):
    exts = face.calcExtension()
    truths = []
    for vertex in gramRun.vertices:
        truths.append(calc.vertexComp(exts[0],vertex))
    if True not in truths:
        newVertex = exts[0]
    else:
        newVertex = exts[1]

    newFaces = []
    oldVs = face.getVertices()
    newFaces.append(Face(paramsList[0],oldVs[0],oldVs[1],newVertex))
    newFaces.append(Face(paramsList[1],oldVs[1],oldVs[2],newVertex))
    newFaces.append(Face(paramsList[2],oldVs[2],oldVs[0],newVertex))

    return (newFaces,newVertex)
        

# This dictionary maps the string id of each operation to the actual function
opMap = {"relabel":relabel, "grow",grow}


###
# this sets up a grammar run given a string genome mapping, and a configuration type
# (for now just the default one). It then returns the GrammarRun object
###
def startGrammarRun(geneDict,setup="default"):
    run = GR()
    
    prodDict = {}
    for lhs,rhs in geneDict.items():
        opString = rhs[0]
        paramList = rhs[1]
        oper = opMap[opString]
        prodDict[lhs] = (oper,paramList)

    if setup == "default":
        faceList = fb.buildDefaultTetra():

    run.setup(prodDict,faceList)
    return run
