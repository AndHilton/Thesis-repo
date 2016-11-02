### ------------------------------------------------------------
"""
This class holds all of the information needed for a given configuration
of the grammar.  I think that having it reside in a class rather than a
procedure allows a little bit more flexibility in the way that it is setup
and run.

Author : AHilton
"""
### ------------------------------------------------------------

import numpy as np
import math
from Face import Face
import facebuilder as fb
from collections import deque
import calculations as calc

class GrammarRun:

    productions = None
    faceQueue = None
    vertices = None

    def __init__(self):
        self.productions = {}
        self.faceQueue = deque()
        self.vertices = []

    ###
    # Sets up the initial configuration of the system given an initial list of faces
    # and a dictionary containing production rules
    ###
    def setup(self,prodDict,initialFaceList):
        self.productions = prodDict
        for face in initialFaceList:
            self.faceQueue.append(face)
            for vertex in face.getVertices():
                found = False
                counter = 0
                while counter < len(self.vertices) and not found:
                    found = calc.vertexComp(vertex,self.vertices[counter])
                    counter += 1


    
    ###
    # goes through a single iteration of productions of the grammar
    ###
    def nextStep(self):
        newQueue = deque()
        while len(self.faceQueue) > 0:
            current = self.faceQueue.popleft()
            lhs = current.label
            rhs = self.productions[lhs]
            operation = rhs[0]
            paramsList = rhs[1]
            result = operation(self,paramsList)
            newQueue.extend(result[0])
            if result[1] != None:
                self.vertices.append[result]
        self.faceQueue = newQueue


    
    ###
    # does n number of iterations
    ###
    def nRun(self,n):
        for i in range(n):
            self.nextStep()
    
