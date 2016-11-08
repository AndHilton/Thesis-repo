### ------------------------------------------------------------
"""
Provides tools to add geometric elements to the current scene of
the blender project
"""
### ------------------------------------------------------------

import bpy
import modeling


###
# adds a tetrahedral face to the scene
#
# takes a list of 3 float tuples representing the vertices
# in as an argument
#
# also takes in a name
###
def add_tetraFace(vertList,name):

    edges = [[0,1],[1,2],[2,0]]
    faces = [[1,2,3]]
    
    meshName = name + "_data"
    faceMesh = bpy.data.meshes.new(meshName)
    faceMesh.from_pydata(vertList,edges,[])
    #faceMesh.show_double_sided = True
    faceMesh.update(calc_tessface=True)

    faceObj = bpy.data.objects.new(name,faceMesh)

    bpy.context.scene.objects.link(faceObj)

    
