### ------------------------------------------------------------
"""
Testing out creating faces using the blender api
"""
### ------------------------------------------------------------

import bpy
import numpy as np
import math


def main():

    print("Testing out Blender API")
    add_plane_default()
    add_face_default()


###
# Adds a flat plane to the scene
###
def add_plane_default():

    # defines vertices and faces
    verts = [(0,0,0),(0,5,0),(5,5,0),(5,0,0)]
    faces = [(1,2,3,4)]

    # defines mesh and object variables
    myMesh = bpy.data.meshes.new("Plane")
    myObject = bpy.data.objects.new("Plane",myMesh)

    # set the location and scene of the object
    myObject.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(myObject)

    # create mesh
    myMesh.from_pydata(verts,[],faces)
    myMesh.update(calc_edges=True)


###
# adds a face to the scene
###
def add_face_default():

    verts = [(0,0,0),(1,0,0),(1/2,math.sqrt(3)/2,0)]
    faces = [(1,2,3)]

    myMesh = bpy.data.meshes.new("Face")
    myObject = bpy.data.objects.new("Face",myMesh)

    bpy.context.scene.objects.link(myObject)

    myMesh.from_pydata(verts,[],faces)
    myMesh.update(calc_edges=True)
             

    

if __name__ == "__main__":
    main()
