### -----------------------------------------------------------------
"""
A trial to optimize for the volume of the convex hull
"""
### -----------------------------------------------------------------

import grammar as gram
import mp_evo
import modeling
import trials


def main():

    gens = 50
    pop = 50
    t = 10
    ffun = trials.maxConvexVol
    erun = mp_evo.executeRun(ffun,gens,pop,t)

    trials.trialTools.outfile(erun,"convexhull")
    trials.trialTools.saveHistory(erun,"convexhull")

    print("Done!")


if __name__ == "__main__":
    main()
