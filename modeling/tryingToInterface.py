### ------------------------------------------------------------
"""
This script is for testing out different different methods of interfacing
between the grammar system and the modeling system
"""
### ------------------------------------------------------------

import sys
sys.path.insert(0,"/home/ahilton/thesis-repo/")


import bpy
import modeling
import grammar as gram
import numpy as np



def main():

    secString = "\n\n{}\n\n".format("-" * 35)
    
    print("Testing methods of interfacing grammar with Blender")
    print(secString)

    # File constants
    filename = "tryingtointerface_2.blend"
    breakPoints = [0,
                   1,
                   5,
                   10,
                   20,
                   50]
    breakPoints = breakPoints[:4]  # **Modify this to change the range of breakpoints**
    print(breakPoints[-1])
    
    ## Grammar Definition ##
    LHS = ["A","B","C","D","E","F"]
    RHS = [("relabel","E"),
           ("grow","CDA"),
           ("relabel","B"),
           ("rest",""),
           ("grow","FCD"),
           ("relabel","E")]
    ruledic = dict(zip(LHS,RHS))

    print("Testing using the following grammar:")
    for pair in sorted(ruledic.items()):
        print("\t{} --> {}({})".format(pair[0],pair[1][0],pair[1][1]))
    print(secString)
        
    # sets up a grammar run with the given grammar
    myRun = gram.runcontroller.setupRun(ruledic)

    # creates the new file that the meshes produced will be added to
    print("Creating a new Blender project : {}".format(filename),secString)
    modeling.file_tools.save_as(filename)
    
    # adds each of the breakpoint iterations to the project
    print("Beginning to add geometry to the project",secString)
    while myRun.iterNum <= breakPoints[-1]:
        if myRun.iterNum in breakPoints:
            print("Rendering iteration {}".format(myRun.iterNum))
            modeling.file_tools.addScene(sceneName = "iter{}".format(myRun.iterNum))
            faceList = myRun.getFaces()
            for idx in range(len(faceList)):
                curFace = faceList[idx]
                facename = "iter{}_face{}".format(myRun.iterNum,idx)
                arrList = curFace.getVertices()
                tupleList = []
                for orig in arrList:
                    tupleList.append(tuple(orig.tolist()))
                modeling.add_geometry.add_tetraFace(tupleList,facename)
            modeling.file_tools.save()
        myRun.nextStep()

    # should be done now
    print("Saving File")
    modeling.file_tools.save()
    
    



if __name__ == "__main__":
    main()
