### ------------------------------------------------------------
"""
a module that provides an interface between the Grammar productions
and the other parts of the system

Author : AHilton
"""
### ------------------------------------------------------------

import numpy as np
from grammar import Face
from grammar import GrammarRun as GR
from grammar import calculations as calc
from grammar import facebuilder as fb


### ------------------------- ###
###     GRAMMAR OPERATIONS    ###
### ------------------------- ###

# GRAM_OPS = [relabel,grow,rest]

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
    return [face]


###
# the function for the grow operation of the grammar
# takes in a grammar run, the face being operated on, and a list
# containing the label for the new faces being produced
#
# returns a tuple containing a list of the new faces, and the new Vertex
###
def grow(gramRun,face,paramsList):
    face.changeLabel("none")
    if growIntersects(face,gramRun.getFaces()):
        return [face]
    else:
        newFaces = [face]
        oldVs = face.getVertices()
        newFaces.append(Face(paramsList[0],[oldVs[0],oldVs[1],newVertex],oldVs[2]))
        newFaces.append(Face(paramsList[1],[oldVs[1],oldVs[2],newVertex],oldVs[0]))
        newFaces.append(Face(paramsList[2],[oldVs[2],oldVs[0],newVertex],oldVs[1]))
        return newFaces


###
# the function for the rest operation of the grammar
# takes in a grammar run, the face being operated on, and an empty list
#
# returns a tuple containing a list containing the original face, and None
###
def rest(gramRun,face,paramsList):
    return [face]

###
# goes through the list of faces and checks to see if the current face
# intersects any of them
###
def growIntersects(curFace,faceList):
    stop = False
    i = 0
    while i < len(faceList) and not stop:
        stop = calc.isGrowIntersect(curFace,faceList[i])
        i += 1
    return stop

# This dictionary maps the string id of each operation to the actual function
opMap = {"relabel":relabel, "grow":grow, "rest":rest}


###
# this sets up a grammar run given a string genome mapping, and a configuration type
# (for now just the default one). It then returns the GrammarRun object
# ****DEPRECATED*****
# From now on use the setupRun function
###
def startGrammarRun(geneDict,setup="default"):
    run = GR()
    
    prodDict = {"none" : (rest,"")}
    for lhs,rhs in geneDict.items():
        opString = rhs[0]
        paramList = list(rhs[1])
        oper = opMap[opString]
        prodDict[lhs] = (oper,paramList)

    faceList = fb.buildDefaultTetra(setup)

    run.setup(prodDict,faceList)
    return run

###
# has the same functionality of the startGrammarRun function, but with a better name
###
def setupRun(genedict,setup="default"):

    # This is going to be the function where I will add the functionality of the different
    # setup paramters (like initial face labels, etc.)
    return startGrammarRun(genedict,setup)
