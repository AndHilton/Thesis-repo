### ------------------------------------------------------------
"""
the Face class is used to represent the Faces operated on
by the grammar.  They keep track of the 3 vertices that define
the Face, as well as the label that the face has

Author: AHilton
"""
### ------------------------------------------------------------

import numpy as np
import Vertex

class Face:

    vertices = None
    label = None

    def __init__(self,alabel,vert0,vert1,vert2):

        self.label = alabel
        self.vertices = [vert0,vert1,vert2]


    ##
    # Changes the label of the face
    ##
    def change_label(self,alabel):
        self.label = alabel
    
