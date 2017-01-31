### ------------------------------------------------------------
"""
Does a series of productions with grow and rest in order to see
if grow is behaving correctly
"""
### ------------------------------------------------------------

import sys
sys.path.insert(0,"/home/ahilton/thesis-repo/")

import bpy
import grammar
import modeling
import numpy as np


def main():

    ## File Constants ##
    filename = "watching_grow.blend"
    modeling.file_tools.save_as(filename)

    ## Production Rules ##
    #LHS = ["A","B","C","D"]
    ruledic = {"A" : ("rest",""),
           "B" : ("rest",""),
           "C" : ("rest",""),
           "D" : ("grow","BCD")}

    gr = grammar.runcontroller.setupRun(ruledic)

    runNum = 10
    while gr.iterNum <= runNum:
        modeling.file_tools.addScene("iter{}".format(gr.iterNum))
        modeling.gramConversion.modelGrammar(gr)
        gr.nextStep()

    modeling.file_tools.save()



if __name__ == "__main__":
    main()
