### -----------------------------------------------------------------
"""
Module: populate.py

This module handles the creation of populations of grammar runs

Author: AHilton
"""
### -----------------------------------------------------------------

import grammar as gram
from grammar import runcontroller as control
from grammar import GrammarRun as Run
import random

LABEL_START = ord("A")
<<<<<<< HEAD
MAX_LABELS = 8
=======
MAX_LABELS = 6
>>>>>>> evosys
MIN_LABELS = 4
OPER_LIST = ["grow","relabel","rest"]

###
# returns a list of k random grammars
###
def kPopulation(k):
    return [makeRandomGram() for i in range(k)]

###
# creates a randomized grammar with between MIN_LABELS and a specified
# number of max_labels (default MAX_LABELS) and returns a GrammarRun
# object with the specified rules
###
<<<<<<< HEAD
def makeRandomGram(max_num = MAX_LABELS,start="default"):
    labels = generateLabels(max_num)
=======
def makeRandomGram(start="default"):
    labels = generateLabels()
>>>>>>> evosys
    ruledic = generateRuleDic(labels)
    if start == "random":
        start = ["random",list(ruledic.keys())]
    return control.setupRun(ruledic,start)

###
<<<<<<< HEAD
# generates a list of labels between the MIN_LABELS and the given max
# length
###
def generateLabels(max_len = MAX_LABELS):
=======
# returns the list of labels starting from 'A' to the MAX_LABELS
###
def generateLabels():
    return [chr(x) for x in range(LABEL_START,LABEL_START+MAX_LABELS)]

###
# generates a list of labels between the MIN_LABELS and the given max
# length
###
def generateRandomLabels(max_len = MAX_LABELS):
>>>>>>> evosys
    n = random.randint(MIN_LABELS,max_len)
    return [chr(x) for x in range(LABEL_START,LABEL_START+n)]

###
# creates a rule dictionary given a pool of labels
###
def generateRuleDic(labelPool):
    rhs = []
    for letter in labelPool:
        oper = random.choice(OPER_LIST)
        if oper == "grow":
            args = ""
            for i in range(3):
                args += random.choice(labelPool)
        elif oper == "relabel":
            labelchoices = labelPool.copy()
            labelchoices.remove(letter)
            args = random.choice(labelchoices)
        elif oper == "rest":
            args = ""
        rhs.append((oper,args))
    ruledic = dict(zip(labelPool,rhs))
    return ruledic
