import os


def path():
    '''
    abspath: return the absolute path
    realpath: return the real path of a link file
    dirname: Returns the directory of a path#
    listdir: list all the elements in the dir

    below result is :
    C:/Users/moochergaga/project/Flaskpractise/filepath.py
    C:/Users/moochergaga/project/Flaskpractise
    C:/Users/moochergaga/project/Flaskpractise
    ['filepath.py', 'hello.py', 'mailtest.py', 'matplotlib', 'templates']
    C:/Users/moochergaga/project/Flaskpractise/filepath.py
    C:/Users/moochergaga/project/Flaskpractise/hello.py
    C:/Users/moochergaga/project/Flaskpractise/mailtest.py
    C:/Users/moochergaga/project/Flaskpractise/matplotlib
    C:/Users/moochergaga/project/Flaskpractise/templates

    '''

    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.dirname(os.path.realpath(__file__)))

    filelist = os.listdir('C:/Users/moochergaga/project/Flaskpractise')
    print(filelist)

    for file in filelist:
        print((os.path.realpath(file)))


path()
