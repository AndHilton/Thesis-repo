
import bpy


def main():
    print("Testing just saving an empty file")

    bpy.ops.wm.save_as_mainfile(filepath="/home/ahilton/thesis-repo/modeling/thisshouldsave.blend")



if __name__ == "__main__":
    main()
