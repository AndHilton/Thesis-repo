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
from grammar import Face
from grammar import facebuilder as fb
from collections import deque
from grammar import calculations as calc

class GrammarRun:

    productions = None
    opQueue = None
    faces = None
    isSetup = False
    iterNum = 0

    def __init__(self):
        self.productions = {}
        self.opQueue = deque()
        self.faces = []

    ###
    # Sets up the initial configuration of the system given an initial list of faces
    # and a dictionary containing production rules
    ###
    def setup(self,prodDict,initialFaceList):
        self.productions = prodDict
        self.faces = initialFaceList
        for face in initialFaceList:
            self.opQueue.append(face)
        self.isSetup = True
                        

    
    ###
    # goes through a single iteration of productions of the grammar
    ###
    def nextStep(self):
        newQueue = deque()
        while len(self.opQueue) > 0:
            current = self.opQueue.popleft()
            lhs = current.label
            rhs = self.productions[lhs]
            operation = rhs[0]
            paramsList = rhs[1]
            result = operation(self,current,paramsList)
            newQueue.extend(result)
            self.faces += [item for item in result if item not in self.faces]
#            if result[1]:
#                newQueue.append(current)
#            elif result[0] is not None:
#                self.faces += result[0]
#                newQueue.extend(result[0])
        self.opQueue = newQueue
        self.iterNum += 1


    
    ###
    # does n number of iterations
    ###
    def nRun(self,n):
        for i in range(n):
            self.nextStep()
    


    ###
    # returns a grammar-string representation of the current state of the system
    # (i.e. returns a string of labels, in the order of the queue)
    ###
    def stringRep(self):
        retStr = ""
        for current in self.getFaces():
            if current.label == "none":
                retStr += "x"
            else:
                retStr += current.label
        return retStr

    ###
    # returns the list of faces currently being tracked in the system
    ###
    def getFaces(self):
        return list(self.opQueue)
        #return self.faces
    
    ###
    # returns a string representation of the grammar
    ###
    def grammarString(self):
        nonTerms = [x for x in self.productions.keys() if x != "none"]
        nonTerms.sort()
        retStr = ""
        for lhs in nonTerms:
            retStr += "{}  -->  {}\n".format(lhs,self.productions[lhs][1])
        return retStr[:-1]

    ###
    # returns the genotype of the grammar, which is a dictionary of the
    # grammar rules
    ###
    def genotype(self):
        genes = self.productions.copy()
        del genes["none"]
        return genes
