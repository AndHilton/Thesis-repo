### -----------------------------------------------------------------
"""
A Trial to try and minimize the density based on the bounded volume
and the number of faces
"""
### -----------------------------------------------------------------

import grammar as gram
import mp_evo
import modeling
import trials

def main():

    gens = 50
    pop = 25
    t = 8
    ffun = trials.minBoundedDensity
    erun = mp_evo.executeRun(ffun,gens,pop,t)

    trials.trialTools.outfile(erun,"minbound-density_{}".format(erun.runID()))
    trials.trialTools.saveHistory(erun,"minbound-density_{}".format(erun.runID()))

    print("Done!")

if __name__ == "__main__":
    main()
