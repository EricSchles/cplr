from subprocess import call
import os
import shutil

def setup_file(filename):
    filename = filename.split(".py")[0] + ".pyx"
    setup_py = """
from distutils.core import setup
from Cython.Build import cythonize
    
setup(
  ext_modules = cythonize(\""""+filename+"""\")
)
"""
  
    with open("setup.py","w") as f:
        f.write(setup_py)
    return setup_py

def build(filename):
    directory = filename.split(".py")[0]
    os.chdir(directory)
    call(["python","setup.py","build_ext","--inplace"])
    return "success"

def create_pyx_file(filename):
    pyx_file = filename.split(".py")[0] + ".pyx"
    with open(filename,"r") as f:
        content = f.read()
    with open(pyx_file,"w") as f:
        f.write(content)
    return "success"

def move_files(filename):
    directory = filename.split(".py")[0]
    pyx_file = filename.split(".py")[0]+".pyx"
    if not os.path.exists(directory):
        os.mkdir(directory)
    shutil.copyfile("setup.py",directory+"/setup.py")
    shutil.copyfile(filename,directory+"/"+pyx_file)
    os.remove("setup.py")
    os.remove(pyx_file)

def compile(filename):
    create_pyx_file(filename)
    setup_file(filename)
    move_files(filename)
    build(filename)

if __name__ == '__main__':
    from sys import argv
    filename = argv[1]
    print "create pyx file"
    create_pyx_file(filename)
    print "create setup.py file"
    setup_file(filename)
    print "creating build directory"
    move_files(filename)
    print "compiling"
    build(filename)
    
