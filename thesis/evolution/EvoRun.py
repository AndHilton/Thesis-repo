### -----------------------------------------------------------------
"""
Class: EvoRun

The EvoRun class is responsible for handling the functionality and data
for individual evolutionary runs of the whole system.  Each instance of
the class will be passed a starting size, and a heuristic search function.

The instance can then be asked to run a given number of generations on the
original population.

Author : AHilton
"""
### -----------------------------------------------------------------

import grammar as gram
import evolution as evo
import grammar.GrammarRun as gRun
import evolution.populate as pop
import evolution.evoOps as ops
import random

#SEED_RANGE = 10 ** 5

class EvoRun:

    id_num = 0
    searchFun = None
    population = None
    iterNum = 0
    generation = 0
    mature = False
    tops = []

    def __init__(self,hSearch,iterNum,k,seed=None):
        if seed is None:
            self.id_num = random.random()
        else:
            self.id_num = seed
        self.searchFun = hSearch
        self.iterNum = iterNum
        self.population = pop.kPopulation(k,self.id_num)
        self.tops = []

    ##
    # applies production rules to each individual in the population
    ##
    def maturePopulation(self):
        if not self.mature:
            for gram in self.population:
                gram.nRun(self.iterNum)
            self.mature = True

    ##
    # returns a list of every individual paired with its fitness score
    ##
    def applySearch(self):
        return [(gram,self.searchFun(gram)) for gram in self.population]


    ##
x    # returns a list of the scores of a generation
    ##
    def getScores(self):
        pairs = self.applySearch()
        scores = [p[1] for p in pairs]
        return scores
    ##
    # returns the most-fit individual in the current population
    ##
    def getAlpha_individual(self,pop=None):
        return self.getAlpha(pop)[0]

    def getAlpha(self,pop=None):
        if pop is None:
            self.maturePopulation()
            pop = self.applySearch()
        return max(pop,key=lambda pair: pair[1])

    def getAlpha_score(self,pop=None):
        return self.getAlpha(pop)[1]

    ##
    # returns a list containing all of the alpha individuals for every generation
    ##
    def history(self):
        return self.tops
    
    ##
    # forwards the generation by 1
    ##
    def nextGeneration(self):
        self.maturePopulation()
        #print("Propagating Generation {}".format(self.generation))
        scores = self.applySearch()
        self.population = ops.propagate(scores)
        self.tops.append(self.getAlpha_individual(scores))
        self.generation += 1
        self.mature = False

    ##
    # simulates n generations of the run
    ##
    def nGeneration(self,n):
        for i in range(n):
            self.nextGeneration()

    ##
    # gets the identifier for the run
    ##
    def runID(self):
        return "run_{}".format(str(self.id_num)[2:])
    
