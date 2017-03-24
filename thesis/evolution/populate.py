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
MAX_LABELS = 8
MIN_LABELS = 4
OPER_LIST = ["grow","relabel","rest"]

###
# creates a randomized grammar with between MIN_LABELS and a specified
# number of max_labels (default MAX_LABELS) and returns a GrammarRun
# object with the specified rules
###
def makeRandomGram(max_num = MAX_LABELS):
    labels = generateLabels(max_num)
    ruledic = generateRuleDic(labels)
    return control.setupRun(ruledic)

###
# generates a list of labels between the MIN_LABELS and the given max
# length
###
def generateLabels(max_len = MAX_LABELS):
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