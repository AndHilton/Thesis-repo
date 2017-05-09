### ------------------------------------------------------------
"""
The init file for the modeling package

Includes:
  -the saving_tools module
  -the add_geometry module
"""
### ------------------------------------------------------------

#import sys
#sys.path.insert(0,"/home/ahilton/thesis-repo/grammar/")
#sys.path.insert(0,"/home/ahilton/thesis-repo/modeling/")

try:
    import bpy
except ImportError:
    pass
else:
    import file_tools
    import add_geometry
from modeling.gramConversion import outputSTL
