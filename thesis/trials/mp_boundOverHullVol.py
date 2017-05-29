### -----------------------------------------------------------------
"""
A trial to optimize for the bounded volume over the volume of the
convex hull
"""
### -----------------------------------------------------------------

import grammar as gram
import mp_evo
import modeling
import trials

def main():

    gens = 25
    pop = 20
    t = 8
    ffun = trials.boundOverHullVol
    erun = mp_evo.executeRun(ffun,gens,pop,t)

    trials.trialTools.outfile(erun,"maxbound-minhull_{}".format(erun.runID()))
    trials.trialTools.saveHistory(erun,"maxbound-minhull_{}".format(erun.runID()))

    print("Done!")


if __name__ == "__main__":
    main()
