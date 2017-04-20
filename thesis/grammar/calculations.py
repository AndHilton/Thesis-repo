### ------------------------------------------------------------
"""
Just some utility functions used to calculate metrics about
faces and whatnot
"""
### ------------------------------------------------------------

import numpy as np
import math


THRESHOLD = 10**(-12)

###
# calculates if 2 vertices are "equal" based on a default threshold
# returns true if the vertices are within 
###
def vertexEq(A,B):
    return np.linalg.norm(abs(A-B)) < THRESHOLD

###
# goes through a list of vertices and returns the index of the one which is closest
# to the origin
###
def findClosest(vertList):
    origin = np.array([0,0,0])
    distList = [np.linalg.norm(abs(x-origin)) for x in vertList]
    mindex = distList.index(min(distList))
    return mindex

###
# returns true iff the vertex is an element of the given list of vertices
###
def isVert_inList(avert,vertlist):
    found = False
    idx = 0
    while idx < len(vertlist) and not found:
        found = vertexEq(avert,vertlist[idx])
        idx += 1
    return found

###
# calculates a tuple of two points that would be extensions of the face
# defined by the list of points given
###
def face_extension(vertlist):
    height = math.sqrt(2/3)
    pVec = vertlist[0]
    vertsPrime = [vec - pVec for vec in vertlist]
    uVec = vertsPrime[1]
    vVec = vertsPrime[2]
    cVec = sum(vertsPrime)/len(vertsPrime)
    ortho = np.cross(uVec,vVec)
    scaleOrtho = ortho/np.linalg.norm(ortho) * height
    extend = (scaleOrtho + cVec) + pVec
    minus_extend = (-1 * scaleOrtho + cVec) + pVec
    return (extend,minus_extend)


###
# takes in an origin face and a test face, and determines whether or not
# a grow operation would intersect the bounds of another face
#
# returns true iff a grow operation on origin would intersect with target
###
def isGrowIntersect(origin,target):
    verts = origin.getVertices()
    stop = False
    i = 0
    while i < len(verts) and not stop:
        p = pointOnPlane(verts[1],origin.growOut(),target.center(),target.vecNorm())
        stop = isPointInBounds(p,target)
        i += 1
    return stop

###
# the old version of the isGrowIntersect which just checks the line from the center
# to the extension
###
def old_isGrowIntersect(origin,target):
    p = pointOnPlane(origin.center(),origin.growOut(),target.center(),target.vecNorm())
    return isPointinBounds(p,target)

###
# calculates the point in where a given line segment intersects the plane
# described by a point and a normal vector if such a point exists
#
# returns a numpy array representing the point or None if the segment
# does not intersect
###
def pointOnPlane(P_0,P_1,V_0,n):
    u = P_1 - P_0
    if is_lineplane_parallel(u,n):
        if is_line_onplane(P_0,V_0,n):
            return u / 2
        else:
            return None
    else:
        w = P_0 - V_0
        s = np.dot(-n,w) / np.dot(n,u)
        if s >= 0 and s <= 1:
            return P_0 + s * u
        else:
            return None

###
# determines whether or not a given vector is parallel to the plane with the
# ortho-normal vector n
###
def is_lineplane_parallel(u,n):
    return np.dot(u,n) == 0

###
# determines whether or not a line containing p lies on the plane determined
# by V_0 and n
###
def is_line_onplane(p,V_0,n):
    return np.dot(n,(p-V_0)) == 0


###
# determines whether a given point is within the bounds of the target face
###
def isPointInBounds(point,faceTar):
    if point is None:
        return False
    else:
        verts = faceTar.getVertices()
        return isSameSide(point,verts[0],verts[1],verts[2]) and isSameSide(point,verts[1],verts[0],verts[2]) and isSameSide(point,verts[2],verts[0],verts[1])

###
# determines if point1 falls on the same side of the line (b-a) as point2
###
def isSameSide(p1,p2,a,b):
    cross1 = np.cross(b-a,p1-a)
    cross2 = np.cross(b-a,p2-a)
    return np.dot(cross1,cross2) >= 0


###
# returns the volume of the bounding box around a GrammarRun
###
def grammarBoundsVolume(gRun):
    bounds = gRun.getBounds()
    dims = [pair[1] - pair[0] for pair in bounds]
    vol = 1
    for scale in dims:
        vol *= scale
    return vol
