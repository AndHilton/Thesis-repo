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

    gens = 25
    pop = 20
    t = 8
    ffun = trials.maxConvexVol
    erun = mp_evo.executeRun(ffun,gens,pop,t)

    trials.trialTools.outfile(erun,"convexhull")
    trials.trialTools.saveHistory(erun,"convexhull")

    print("Done!")


if __name__ == "__main__":
    main()
