### ------------------------------------------------------------
"""
This script takes gram14, and converts it to an stl
"""
### ------------------------------------------------------------

import sys
sys.path.insert(0,"/home/ahilton/thesis-repo/")

import modeling
import grammar
from gram14 import getGram14


def main():

    ## File Constants ##
    blendfile = "gram14.blend"
    stlfile = "gram14.stl"

    modeling.file_tools.save_as(blendfile)
    
    # all hail
    g14 = getGram14()

    n = 10
    g14.nRun(n)

    modeling.gramConversion.modelGrammar(g14)
    modeling.file_tools.save()

    modeling.gramConversion.outputSTL(g14,stlfile)

    




if __name__ == "__main__":
    main()
