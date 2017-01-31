### ------------------------------------------------------------
"""
This is just a script to test out the various grammar configurations
"""
### ------------------------------------------------------------

import sys
sys.path.insert(0,"/home/ahilton/thesis-repo/")

import bpy
import modeling
import grammar



def main():

    ## File Constants ##
    filename = "testing_grams.blend"
    stlfile = "blenderfiles/testing_grams.stl"
    modeling.file_tools.save_as(filename)

    ## Production Rules ##
    ruledic = {"A" : ("grow","CCB"),
               "B" : ("rest",""),
               "C" : ("rest",""),
               "D" : ("grow","EBE"),
               "E" : ("rest",""),
               "F" : ("rest",""),
               "G" : ("relabel","D")}

    print("Modeling Grammar")
    for pair in sorted(ruledic.items()):
        print("\t{} --> {}({})".format(pair[0],pair[1][0],pair[1][1]))
        
    gr = grammar.runcontroller.setupRun(ruledic)

    runNum = 5
    gr.nRun(runNum)
    modeling.gramConversion.modelGrammar(gr)

    modeling.file_tools.save()

    modeling.gramConversion.outputSTL(gr,stlfile)






if __name__ == "__main__":
    main()
