import sys

print(dir(sys))
print(dir('alina'))
print(dir([]))

print(dir(str) == dir(''))

"""
Module documentation
Words Go Here
"""

spam = 40


def square(x):
    """
    function documentation
    can we have your liver then?
    """
    return x ** 2


class Employee:
    "class documentation"
    pass

print(square(4))
print(square.__doc__)
print(Employee.__doc__)

print(sys.__doc__)
print(sys.getrefcount.__doc__)

print(abs.__doc__)

print(help(sys.getcheckinterval))