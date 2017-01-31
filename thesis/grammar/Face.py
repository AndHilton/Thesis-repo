### ------------------------------------------------------------
"""
the Face class is used to represent the Faces operated on
by the grammar.  They keep track of the 3 vertices that define
the Face, as well as the label that the face has

Author: AHilton
"""
### ------------------------------------------------------------

import numpy as np
import math
import calculations

class Face:

    vertices = None
    label = None

    def __init__(self,alabel,vert0,vert1,vert2):

        self.label = alabel
        self.vertices = [vert0,vert1,vert2]


    ##
    # Changes the label of the face
    ##
    def changeLabel(self,alabel):
        self.label = alabel

    ##
    # Returns the list of vertices
    ##
    def getVertices(self):
        return self.vertices

    ##
    # Calculates the positions of the 2 possible extensions of the face.  Returns the two vertices as a tuple
    ##
    def calcExtension(self):

#        pVec = self.vertices[calculations.findClosest(self.vertices)]
#        vertsMinus = self.vertices.copy().remove(pVec)
        pVec = self.vertices[0]
        vertPrime = [vec - pVec for vec in self.vertices]
        uVec = vertPrime[1]
        vVec = vertPrime[2]
        height = math.sqrt(2/3)     # this is for the Python 3 version
        cVec = sum(vertPrime)/len(vertPrime)

        ortho = np.cross(uVec,vVec)
        scaleOrtho = ortho/np.linalg.norm(ortho) * height
        extend = (scaleOrtho + cVec) + pVec
        return (extend,-extend)
    
