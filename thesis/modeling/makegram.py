### ------------------------------------------------------------
"""
Just makes an stl of the grammar given

This will be a lot simpler whenever I have separated the blender
functionality from the generic modeling package
"""
### ------------------------------------------------------------

import sys
sys.path.insert(0,"/home/ahilton/thesis-repo/")

import grammar

thisGramRules = {"A" : ("grow","CBD"),
                 "B" : ("rest",""),
                 "C" : ("grow","BDC"),
                 "D" : ("grow","DBD")}

runlength = 10
filename = "blenderfiles/balls.stl"

def main() :
    gram = grammar.runcontroller.setupRun(thisGramRules)
    gram.nRun(runlength)
    outputSTL(gram,filename)
    
###
# takes a GrammarRun object, and writes its current configuration
# to an STL file
###
def outputSTL(gramRun,filename):
    print("Writing grammar to {}".format(filename))
    f = open(filename,"w")
    f.write("solid foo\n")
    for face in gramRun.getFaces():
        f.write(face_toSTL(face))
    f.write("endsolid foo")
    f.close

###
# takes a grammar Face and returns a string conversion to stl
###
def face_toSTL(face):
    retstr = ""
    retstr += "facet normal 0 0 0\n"
    retstr += "outer loop\n"
    for vert in face.getVertices():
        retstr += "vertex {} {} {}\n".format(vert[0],vert[1],vert[2])
    retstr += "endloop\n"
    retstr += "endfacet\n"
    return retstr



if __name__ == "__main__":
    main()




