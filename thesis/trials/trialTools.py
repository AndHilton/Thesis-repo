### -----------------------------------------------------------------
"""
Module : trialTools.py
Author : AHilton

This
"""
### -----------------------------------------------------------------

import trials
import evolution as evo
import grammar as gram
import modeling
import os


###
# saves the entire history of an EvoRun to a directory
###
def saveHistory(erun,fitness=""):
    dirpath = "data/{}_{}_alphas".format(fitness,erun.runID())
    file_temp = "{}/gen_{}.gram"
    os.mkdir(dirpath)
    hist = erun.history()
    for i in range(len(hist)):
        filename = file_temp.format(dirpath,i)
        gram.saveGrammar(hist[i],filename)


###
# saves the alpha-individual of a run to a default filename
###
def outfile(erun,fitness=""):
    alpha = erun.getAlpha_individual()
    filename = "outputs/{}_{}_alpha.stl".format(fitness,erun.runID())
    modeling.outputSTL(alpha,filename)
    
    
