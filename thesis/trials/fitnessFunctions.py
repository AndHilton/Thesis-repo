### -----------------------------------------------------------------
"""
A collection of various fitness functions used in the trials
"""
### -----------------------------------------------------------------

import grammar as gram

###
# Optimizes for maximum ConvexHull volume
###
def maxConvexVol(grun):
    return geo.convexHullVol(grun)
