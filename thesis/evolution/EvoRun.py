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


class EvoRun:

    searchFun = None
    population = None
    iterNum = 0
    generation = 0
    mature = False

    def __init__(self,hSearch,iterNum,k):
        self.searchFun = hSearch
        self.iterNum = iterNum
        self.population = pop.kPopulation(k)

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
    # returns a list of the scores of a generation
    ##
    def getScores(self):
        pairs = self.applySearch()
        scores = [p[1] for p in pairs]
        return scores
    ##
    # returns the most-fit individual in the current population
    ##
    def getAlpha_individual(self):
        return self.getAlpha()[0]

    def getAlpha(self):
        self.maturePopulation()
        return max(self.applySearch(),key=lambda pair: pair[1])

    def getAlpha_score(self):
        return self.getAlpha()[1]

    ##
    # forwards the generation by 1
    ##
    def nextGeneration(self):
        self.maturePopulation()
        print("Propagating Generation {}".format(self.generation))
        self.population = ops.propagate(self.applySearch())
        self.generation += 1
        self.mature = False

    ##
    # simulates n generations of the run
    ##
    def nGeneration(self,n):
        for i in range(n):
            self.nextGeneration()
