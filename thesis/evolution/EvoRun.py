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

import grammar.runcontroller as crtl
import grammar.GrammarRun as gRun
import evolution.populate as pop

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
            

