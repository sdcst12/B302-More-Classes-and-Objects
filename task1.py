#!python3

class quadratic:
    a = 0
    b = 0
    c = 0
    roots = []

    def discriminant():
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the discriminant which is calculated as 
        # b^2 - 4ac
        # return value should be a float type decimal
        pass
        return
    
    def hasRealRoots():
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine if the quadratic has real roots
        # defined when the discriminant is non negative
        # return value should be True or False
        pass
        return

    def isFactorable():
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine if the quadratic can be factored
        # quadratic can be factored if the discriminant is a perfect square
        # return value is True or False
        pass
        return 
    
    def calcRoots():
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the roots of the quadratic if
        # the quadratic has real roots
        # should make use of the class methods:
        # self.hasRealRoots()
        # self.discriminant
        # method does not have a return value
        # but should store the values of the roots in the 
        # list self.roots
        # list should be sorted in ascending order
        # roots should be rounded to 2 decimal places
        pass

    def __init__():
        # this should require 3 positional arguments and assign the values
        # to self.a, self.b and self.c
        pass



if __name__ == "__main__":
    q1 = quadratic(1,4,4)
    assert q1.isFactorable() == True
    assert q1.hasRealRoots() == True
    assert q1.discriminant() == 0
    assert q1.roots == [-2,-2]

    q2 = quadratic(1,1,-6)
    assert q2.isFactorable() == True
    assert q2.hasRealRoots() == True
    assert q2.discriminant() == 25
    assert q2.roots == [-3,2]

    q3 = quadratic(1,1,10)
    assert q3.isFactorable() == False
    assert q3.hasRealRoots() == False
    assert q3.discriminant() == -39
    assert q3.roots == []

    q4 = quadratic(1,10,1)
    assert q4.isFactorable() == False
    assert q4.hasRealRoots() == True
    assert q4.discriminant() == 96
    assert q4.roots == [-9.90,-0.10]