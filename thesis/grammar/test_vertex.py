### ------------------------------------------------------------
"""
Testing to see if I can maintain the functionality of numpy arrays
while encapsulating them in my own class
"""
### ------------------------------------------------------------

from Vertex import Vertex
import numpy as np


def main():
    print("Testing out constructor and str method")
    test1 = Vertex(1,0,0)
    print(test1)
    print("Testing out how addition and subtraction work")
    test2 = Vertex(0,1,0)
    print("xNorm + yNorm:")
    result = test1 + test2
    print(result)





if __name__ == "__main__":
    main()
