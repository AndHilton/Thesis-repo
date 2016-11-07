### ------------------------------------------------------------
"""
this module provides tools for creating and saving blender files
in order to help the automation process of generating models
"""
### ------------------------------------------------------------


import bpy


###
# creates a new file by saving the default startup file to the given
# filename
#
# takes either the absolute path (with ABSOLUTE=True), or the relative
# path (where the absolute gets set to the default location)
###
def save_as(filename,ABSOLUTE=False):

    DEFAULTPATH="/home/ahilton/thesis-repo/modeling/blenderfiles/"
    if not ABSOLUTE:
        filename = DEFAULTPATH + filename

    bpy.ops.wm.save_as_mainfile(filepath=filename)

###
# just saves the current file
###
def save():
    bpy.ops.wm.save_mainfile()



###
# adds a scene to the current project and switches to it
#
# if a scenename is provided then the new scene will be called that
# otherwise the blender default for new scenes is used
###
def addScene(sceneName=None):
    bpy.ops.scene.new()
    if sceneName is not None:
        bpy.context.scene.name = sceneName
