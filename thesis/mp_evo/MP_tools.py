### -----------------------------------------------------------------
"""
Module : MP_tools.py

a module containing wrapper functions to be used with
multiprocessing Pools
"""
### -----------------------------------------------------------------

import grammar as gram
import evolution as evo
import mp_evo

###
# grows an individual member of a population
###
def matureIndv(bundle):
    gRun = bundle[0]
    n = bundle[1]
    gRun.nRun(n)
    return gRun

###
# evaluates an individual member of the population
###
def evaluateIndv(bundle):
    fun = bundle[1]
    indv = bundle[0]
    return (indv,fun(indv))
