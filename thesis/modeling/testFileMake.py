### ------------------------------------------------------------
"""
tests out the functionality of creating a new blend file through
python and saving it
"""
### ------------------------------------------------------------

import bpy
import math


def main():

    scenename = "testing_saving"
    bpy.ops.scene.new()
    bpy.context.scene.name = scenename

    verts =  [(0,0,0),(1,0,0),(1/2,math.sqrt(3)/2,0),(1/2,1/2*math.sqrt(3),math.sqrt(3/2))]
    verts1 = [verts[0],verts[1],verts[2]]
    verts2 = [verts[0],verts[1],verts[3]]
    verts3 = [verts[0],verts[2],verts[3]]
    verts4 = [verts[1],verts[2],verts[3]]

    add_face(verts1,1)
    add_face(verts2,2)
    add_face(verts3,3)
    add_face(verts4,4)

    bpy.ops.wm.save_mainfile()

def add_face(verts,num):

    faces = [(1,2,3)]

    myMesh = bpy.data.meshes.new("Face{}".format(num))
    myObject = bpy.data.objects.new("Face{}".format(num),myMesh)

    bpy.context.scene.objects.link(myObject)

    myMesh.from_pydata(verts,[],faces)
    myMesh.update(calc_edges=True)
    



if __name__ == "__main__":
    main()
