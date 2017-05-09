### -----------------------------------------------------------------
"""
Has methods that handle the saving and loading of GrammarRun objects
to/from binary files
"""
### -----------------------------------------------------------------

import pickle
import grammar as gram


###
# Takes in a GrammarRun object and a filename and picles the Grammmar Run
###
def saveGrammar(grun,filename):
    f = open(filename,"wb")
    pickle.dump(grun,f)
    f.close()

###
# Reads in a GrammarRun from a binary file and returns the run
###
def loadGrammar(filename):
    f = open(filename,"rb")
    grun = pickle.load(f)
    return grun

###
# Reads a GrammarRun in from a file and returns an instance of that grammar,
# from 0 iterations
###
def reloadGrammar(filename):
    old = loadGrammar(filename)
    prods = old.productions
    faces = gram.facebuilder.buildDefaultTetra()
    new = gram.GrammarRun()
    new.setup(prods,faces)
    return new
