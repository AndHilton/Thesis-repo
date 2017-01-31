### ------------------------------------------------------------
"""
Just some tests on the Face class to make sure that everything
is working as intended
"""
### ------------------------------------------------------------

#import sys
#sys.path.insert(0,"/home/ahilton/thesis-repo/grammar")
import facebuilder
from Face import Face
import numpy as np
import math
import calculations as calc
from itertools import combinations

ERRORVALUE = 10^(12)
threshold = np.array([ERRORVALUE,ERRORVALUE,ERRORVALUE])

def main():

    test_constructor()
    test_extend()
    print("\n\n{}\n\n".format("-"*30))
    test_vertexEq()

    test_facebuild()


def test_constructor():

    print("Testing the Constructor")
    test = build_default_face()
    point1 = np.array([0,0,0])
    point2 = np.array([1,0,0])
    point3 = np.array([1/2,math.sqrt(3)/2,0])
    actual = [point1,point2,point3]
    for i in range(len(test.getVertices())):
        assert np.array_equal(test.getVertices()[i],actual[i])
    assert test.label == "A"

def test_extend():

    print("Testing the calculateExtend method")
    base = build_default_face()
    expected = np.array([1/2,1/(2*math.sqrt(3)),math.sqrt(2/3)])
    actual = base.calcExtension()
    assert np.linalg.norm(actual[0]-expected) < ERRORVALUE or np.linalg.norm(actual[1]-expected) < ERRORVALUE
    assert np.linalg.norm(expected-actual[0]) < ERRORVALUE or np.linalg.norm(expected-actual[1]) < ERRORVALUE

def test_vertexEq():

    print("Testing the vertexEq function in the calculations module")
    xnorm = np.array([1,0,0])
    print("Comparing arrays to {}".format(np.array_str(xnorm)))
    for exp in range(15):
        result = xnorm + np.array([10**(-exp),0,0])
        print("exp = {}".format(-exp))
        print("current = {}".format(np.array_str(result)))
        same = calc.vertexEq(xnorm,result)
        print("are they close enough?  {}".format(same))


def test_facebuild():
    print ("Testing the initial startup conditions of the default setup")
    faces = facebuilder.buildDefaultTetra()
    print("Going through each edge of each face to make sure they are all length 1")
    for face in faces:
        for edgetuple in combinations(face.vertices,2):
            assert np.linalg.norm(edgetuple[0]-edgetuple[1]) == 1
    
def build_default_face():
    label = "A"
    point1 = np.array([0,0,0])
    point2 = np.array([1,0,0])
    point3 = np.array([1/2,math.sqrt(3)/2,0])
    return Face(label,point1,point2,point3)



if __name__ == "__main__":
    main()

