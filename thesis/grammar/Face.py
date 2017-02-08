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
import grammar.calculations as calc

class Face:

    vertices = None
    label = None
    inside = None

    def __init__(self,alabel,vertlist,innervec):

        self.label = alabel
        self.vertices = vertlist
        self.inside = innervec


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
    # Returns the point at the center of the face
    ##
    def centerVec(self):
        return sum(self.vertices)/len(self.vertices)
    
    ##
    # Calculates the positions of the 2 possible extensions of the face.  Returns the two vertices as a tuple
    ##
    def calcExtension(self):

        pVec = self.vertices[0]
        vertPrime = [vec - pVec for vec in self.vertices]
        uVec = vertPrime[1]
        vVec = vertPrime[2]
        height = math.sqrt(2/3)     # this is for the Python 3 version
        cVec = sum(vertPrime)/len(vertPrime)

        ortho = np.cross(uVec,vVec)
        scaleOrtho = ortho/np.linalg.norm(ortho) * height
        extend = (scaleOrtho + cVec) + pVec
        minus_extend = (-1 * scaleOrtho + cVec) + pVec
        return (extend,minus_extend)
    

    ##
    # Calculates the 2 extensions of the face and returns the one pointing out
    ##
    def growOut(self):

        choices = self.calcExtension()
        if calc.vertexEq(self.inside,choices[0]):
            return choices[1]
        else:
            return choices[0]
