### -----------------------------------------------------------------
"""
Module : trial.py

The Trial Module provides the tools to setup and run full evolutionary
runs.  Any script trying to execute a run for results should use these
functions

Author : AHilton
"""
### -----------------------------------------------------------------

import evolution as evo
import modeling as model
import grammar as gram

GENERATION = 100
POPULATION = 50
MATURITY = 10

###
# the main function of this module.  Sets up an EvoRun with the given
# parameters and runs it for the specified number of generations
# returns the run at the end
###
def executeRun(hFun,gen = GENERATION,pop = POPULATION,mature = MATURITY):
    run = evo.EvoRun(hFun,mature,pop)
    print_run_metrics(gen,pop,mature)
    run.nGeneration(gen)
    print_results(run)
    return run

###
# executes an evolutionary run, but logs all the data to a file
# instead of printing to stdout
###
# def executeLoggedRun(hfun,logfile,gen=GENERATION,pop=POPULATION,mature=MATURITY):
#     run = evo.EvoRun(hfun,mature,pop)
#     lines = []
#     lines += metricsStr(gen,pop,mature)
    

###
# prints out the parameters of the run
###
def print_run_metrics(gen,pop,mature):
    sep = "=" * 65 + "\n"
    print("\n")
    print(sep)
    print()
    print(sep)
    print("Evolutionary Parameters")
    print(sep)
    print("\tElitism Rating: {}".format(evo.evoOps.ELITISM))
    print("\tUniform Cross Rate: {}".format(evo.evoOps.UCROSS_RATE))
    print("\tCoarse Mutation Chance: {}%".format(evo.evoOps.COARSE_MUTATION * 100))
    print("\tFine Mutation Chance: {}%".format(evo.evoOps.FINE_MUTATION * 100))
    print()
    print(sep)
    print("Evolutionary Run Metrics")
    print(sep)
    print("\tNumber of Generations: {}".format(gen))
    print("\tSize of Population: {}".format(pop))
    print("\tMaturity of Individuals: t = {}".format(mature))
    print()
    print(sep)

###
# prints the final results of a run
###
def print_results(erun):
    final_scores = erun.getScores()
    avg_score = sum(final_scores)/len(final_scores)
    print("="*65)
    print("Final Results:")
    print("ID: {}".format(erun.runID()))
    print("\tTop Fitness Score: {}".format(erun.getAlpha_score()))
#    print("\tAverage Fitness: {}".format(avg_score))
    print("="*65)
    
