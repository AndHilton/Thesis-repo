### ------------------------------------------------------------
"""
a testing suite for the functionality of the Grammar Run class
(and therefore the grammar system itself)
"""
### ------------------------------------------------------------


import numpy as np
from Face import Face
from GrammarRun import GrammarRun as GR
import runcontroller as control


def main():

    print("GrammarRun and runcontroller testing!")
    test_relabel_oneGen_fourLabel()
    print("\n\n{}\n\n".format("-"*40))
    test_grow_oneGen_oneProd()

###
# tests that a grammar made of just relabel operations gets properly
# iterated over
#
# Grammar:
#   A -> B
#   B -> C
#   C -> D
#   D -> A
#
# also has the added benefit of testing out the setup mechanism
# the iteration mechanism, and the production passing mechanism
#
# has the chance to set a lot of worries aside, or go horribly
# horribly wrong
###
def test_relabel_oneGen_fourLabel():
    print("Testing a grammar of just relabel operations")
    print("Grammar:\n",\
          "A -> B\n",\
          "B -> C\n",\
          "C -> D\n",\
          "D -> A\n")
    stringMap = {"A" : ("relabel",["B"]),
                 "B" : ("relabel",["C"]),
                 "C" : ("relabel",["D"]),
                 "D" : ("relabel",["A"])}
    testRun = control.startGrammarRun(stringMap)
    print("checking the initial setup of the system")
    assert testRun.stringRep() == "ABCD"
    testRun.nextStep()
    print("checing the configuration of the string after one iteration")
    assert testRun.stringRep() == "BCDA"
    

###
# tests that the grow operation works properly over one iteration
###
def test_grow_oneGen_oneProd():
    print("Testing a grammar with one grow operation")
    print("Grammar:\n",
          "A -> BCD\n",
          "B -> A\n",
          "C -> B\n",
          "D -> B\n")
    stringMap = {"A" : ("grow",["B","C","D"]),
                 "B" : ("relabel",["A"]),
                 "C" : ("relabel",["B"]),
                 "D" : ("relabel",["B"])}


    testRun = control.startGrammarRun(stringMap)
    print("checking the initial setup of the system")
    sentence = testRun.stringRep()
    print("initial string: {}".format(sentence))
    assert sentence == "ABCD"
    faceNum = len(testRun.faceQueue)
    print("initial number of faces: {}".format(faceNum))
    assert faceNum == 4
    vertexNum = len(testRun.vertices)
    print("initial number of vertices: {}".format(vertexNum))
    assert vertexNum == 4

    testRun.nextStep()
    print("checking the configuration after 1 iteration")
    sentence = testRun.stringRep()
    expected = "BCDABB"
    print("string: {} = {}?".format(sentence,expected))
    assert sentence == expected
    faceNum = len(testRun.faceQueue)
    print("faces: {} = {}?".format(faceNum,6))
    assert faceNum == 6
    vertexNum = len(testRun.vertices)
    print("vertices: {} = {}?".format(vertexNum,5))
    assert vertexNum == 5

    print("\nGonna keep going to satisfy my curiosity")
    testRun.nextStep()
    sentence = testRun.stringRep()
    expected = "ABBBCDAA"
    print("{} = {}?".format(sentence,expected))
    assert sentence == expected

###
# tests the grammar productions with more than one grow operation
###
## Might do this
          
          
    

if __name__ == "__main__":
    main()
