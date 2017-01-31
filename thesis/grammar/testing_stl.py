### ------------------------------------------------------------
"""
This script is so that I can test out how to actually use the 
STL module to create a viewable model of the system
"""
### ------------------------------------------------------------

import numpy as np
import math
import facebuilder as fb
from Face import Face
from stl import mesh


def main():

    walkthrough1()
    
    base = fb.build_default_face()
    exten = base.calcExtension()
    
    
###
# Goes through the first step of the walkthrough I found
###
def walkthrough1():
    VERTICE_COUNT = 100
    data = np.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
    myMesh = mesh.Mesh(data, remove_empty_areas=False)
    myMesh.save("new_stl_file.stl")



if __name__ == "__main__":
    main()
