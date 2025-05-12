# I will be working on the C++ / Python for the next 90 days

import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Writing my second function to the code base
    def __repr__(self):
        # Printing out a developer friendly function 
        return f"vector {self.x!r} and {self.y!r}"
    
    def __str__(self):
        # printing out the basic version of the print
        return f"{self.x} and {self.y}"
    
    def __abs__(self):
        # Vector addition of the number 
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        # Vector addition
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be of the type vector")
    

    def __scaler__(self, scalar):
        # Vector multiplication
        if isinstance(scalar, Vector):
            return Vector(self.x * scalar.x, self.y * scalar.y)
        raise TypeError("scaler must be a number") 


    
def main():
    v1 = Vector(3, 4)
    v2 = Vector(5, 6)

    print("The first vector is ", v1)
    print("The second vector is", v2)

    # Vector addtion of the two vectors
    print("\n The vector addtion of two vectors are")
    v3 = v1 + v2
    print(repr(v3))

    # Getting the absolute value of the vector
    print(abs(v3))

    # Getting the bool version of the vector
    print(bool(v3))

if __name__ == "__main__":
    main()
