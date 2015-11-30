#Compiler

_By_

_Eric_ _Schles_

This "compiler" leverages Cython.  Cython is extremely easy to use, however, using it can slow down development time (because you have to add in files).  Thus I have created a library which automatically "compiles" python code into it's c equivalent.  Essentially all that I'm doing is taking the .py file and creating a copy that is a .pyx file.  I then compile the .pyx file and save everything into a directory with the same name as the file.

This works great for single file python scripts.  I've still got to think about multi-file python programs.  But one day!

Running the library is very, very easy:

```
from cplr.compiler import compile

compile("test.py")
```

If you look in the current folder, you'll find the compiled code in a seperate folder.  You can then import and use the compiled python code (within the directory that was created).  If you want to use the file globally, you'll need to install it like you would any other python library.  Check out [this project](https://github.com/EricSchles/pshr) for an example for a globally installed python program.  For an explanation of the example check out [this section of the python docs](https://docs.python.org/2/install/)