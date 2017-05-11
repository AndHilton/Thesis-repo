### -----------------------------------------------------------------
"""
Class : MP_EvoRun

This is a subclass of the evolution.EvoRun class that uses the multiprocess
module to parallelize parts of the EvoRun

Author : AHilton
"""
### -----------------------------------------------------------------

import grammar as gram
import evolution as evo
import mp_evo
import multiprocessing as mp

class MP_EvoRun (evo.EvoRun):

    """
    This SubClass is mostly used as a wrapper for multiprocessing functions
    """
    pPool = None

    def __init__(self,hSearch,iterNum,k,seed=None,procnum=1):
        super().__init__(hSearch,iterNum,k,seed)
        self.pPool = mp.Pool(procnum)

    ##
    # Calls on the multiprocess version of maturePopulation
    ##
    def maturePopulation(self):
        if not self.mature:
            bundle = [(gRun,self.iterNum) for gRun in self.population]
            self.population = self.pPool.map(mp_evo.MP_tools.matureIndv,bundle)
        self.mature = True
    
    ##
    # Calls on the multiprocess version of applySearch
    ##
    def applySearch(self):
        bundle = [(gram,self.searchFun) for gram in self.population]
        return self.pPool.map(mp_evo.MP_tools.evaluateIndv,bundle)
