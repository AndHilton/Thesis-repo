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
    return gram.geo.convexHullVol(grun)

###
# Intuition: Will maximize for a large bounded volume, large space covered,
#            but also minize the convex hull, meaning it won't form large
#            ball shapes
###
def boundOverHullVol(grun):
    return gram.geo.grammarBoundsVolume(grun) / gram.geo.convexHullVol(grun)


###
# returns the "density" of the grammar based on the bounded volume and
# the number of faces.  Actually returns the inverse because we want to
# minimize bounded volume
###
def minBoundedDensity(grun):
    return gram.geo.grammarBoundsVolume(grun) / len(grun.getFaces())
