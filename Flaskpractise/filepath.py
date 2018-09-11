import os

basedir = os.path.abspath(os.path.dirname(__file__))


# def abspath(path):
# Return an absolute path.
# def dirname(p):
#Returns the directory component of a pathname#

print(__file__)
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.realpath(__file__)))
