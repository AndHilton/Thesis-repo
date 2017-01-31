### ------------------------------------------------------------
"""
This module just returns a GrammarRun object with the same configuration
as the legendary Gram14, long may it reign
"""
### ------------------------------------------------------------


import sys
sys.path.insert(0,"/home/ahilton/thesis-repo/")

import grammar

###
# the main function of the module, returs Gram14
###
def getGram14():
    ruledic = {"A" : ("grow","CCA"),
               "B" : ("rest",""),
               "C" : ("relabel","D"),
               "D" : ("grow","BBD")}
    gram14 = grammar.runcontroller.setupRun(ruledic)
    return gram14

