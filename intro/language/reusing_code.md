Reusing code: scripts and modules
=================================

For now, we have typed all instructions in the interpreter. For longer
sets of instructions we need to change track and write the code in text
files (using a text editor), that we will call either *scripts* or
*modules*. Use your favorite text editor (provided it offers syntax
highlighting for Python), or the editor that comes with the Scientific
Python Suite you may be using (e.g., Scite with Python(x,y)).

Scripts
-------

> **tip**
>
> Let us first write a *script*, that is a file with a sequence of
> instructions that are executed each time the script is called.
> Instructions may be e.g. copied-and-pasted from the interpreter (but
> take care to respect indentation rules!).

The extension for Python files is `.py`. Write or copy-and-paste the
following lines in a file called `test.py` :

    message = "Hello how are you?"
    for word in message.split():
        print word

> **tip**
>
> Let us now execute the script interactively, that is inside the
> Ipython interpreter. This is maybe the most common use of scripts in
> scientific computing.

> **note**
>
> in Ipython, the syntax to execute a script is `%run script.py`. For
> example,

The script has been executed. Moreover the variables defined in the
script (such as `message`) are now available inside the interpreter's
namespace.

> **tip**
>
> Other interpreters also offer the possibility to execute scripts
> (e.g., `execfile` in the plain Python interpreter, etc.).

It is also possible In order to execute this script as a *standalone
program*, by executing the script inside a shell terminal (Linux/Mac
console or cmd Windows console). For example, if we are in the same
directory as the test.py file, we can execute this in a console:

> **tip**
>
> Standalone scripts may also take command-line arguments
>
> In `file.py`:
>
>     import sys
>     print sys.argv
>
> > **warning**
> >
> > Don't implement option parsing yourself. Use modules such as
> > `optparse`, `argparse` or `docopt`.

Importing objects from modules
------------------------------

And also:

Importing shorthands:

> **warning**
>
>     from os import *
>
> This is called the *star import* and please, **Use it with caution**
>
> -   Makes the code harder to read and understand: where do symbols
>     come from?
> -   Makes it impossible to guess the functionality by the context and
>     the name (hint: os.name is the name of the OS), and to profit
>     usefully from tab completion.
> -   Restricts the variable names you can use: os.name might override
>     name, or vise-versa.
> -   Creates possible name clashes between modules.
> -   Makes the code impossible to statically check for
>     undefined symbols.

> **tip**
>
> Modules are thus a good way to organize code in a hierarchical way.
> Actually, all the scientific computing tools we are going to use are
> modules:
>
>     >>> import numpy as np # data arrays
>     >>> np.linspace(0, 10, 6)
>     array([  0.,   2.,   4.,   6.,   8.,  10.])
>     >>> import scipy # scientific computing

In Python(x,y), Ipython(x,y) executes the following imports at startup:

    >>> import numpy
    >>> import numpy as np
    >>> from pylab import *
    >>> import scipy

and it is not necessary to re-import these modules.

Creating modules
----------------

> **tip**
>
> If we want to write larger and better organized programs (compared to
> simple scripts), where some objects are defined, (variables,
> functions, classes) and that we want to reuse several times, we have
> to create our own *modules*.

Let us create a module `demo` contained in the file `demo.py`:

> **tip**
>
> In this file, we defined two functions `print_a` and `print_b`.
> Suppose we want to call the `print_a` function from the interpreter.
> We could execute the file as a script, but since we just want to have
> access to the function `print_a`, we are rather going to **import it
> as a module**. The syntax is as follows.

Importing the module gives access to its objects, using the
`module.object` syntax. Don't forget to put the module's name before the
object's name, otherwise Python won't recognize the instruction.

Introspection

Importing objects from modules into the main namespace

> **warning**
>
> **Module caching**
>
> > Modules are cached: if you modify `demo.py` and re-import it in the
> > old session, you will get the old one.
>
> Solution:
>
> In Python3 instead `reload` is not builtin, so you have to import the
> `importlib` module first and then do:
>
'\_\_[main](__)' and module loading
-----------------------------------

> **tip**
>
> Sometimes we want code to be executed when a module is run directly,
> but not when it is imported by another module.
> `if __name__ == '__main__'` allows us to check whether the module is
> being run directly.

File `demo2.py`:

Importing it:

Running it:

Scripts or modules? How to organize your code
---------------------------------------------

> **note**
>
> Rule of thumb
>
> -   Sets of instructions that are called several times should be
>     written inside **functions** for better code reusability.
> -   Functions (or other bits of code) that are called from several
>     scripts should be written inside a **module**, so that only the
>     module is imported in the different scripts (do not copy-and-paste
>     your functions in the different scripts!).

### How modules are found and imported

When the `import mymodule` statement is executed, the module `mymodule`
is searched in a given list of directories. This list includes a list of
installation-dependent default path (e.g., `/usr/lib/python`) as well as
the list of directories specified by the environment variable
`PYTHONPATH`.

The list of directories searched by Python is given by the `sys.path`
variable

Modules must be located in the search path, therefore you can:

-   write your own modules within directories already defined in the
    search path (e.g. `$HOME/.local/lib/python2.7/dist-packages`). You
    may use symbolic links (on Linux) to keep the code somewhere else.
-   modify the environment variable `PYTHONPATH` to include the
    directories containing the user-defined modules.

    > **tip**
    >
    > On Linux/Unix, add the following line to a file read by the shell
    > at startup (e.g. /etc/profile, .profile)
    >
    >     export PYTHONPATH=$PYTHONPATH:/home/emma/user_defined_modules
    >
    > On Windows, <http://support.microsoft.com/kb/310519> explains how
    > to handle environment variables.

-   or modify the `sys.path` variable itself within a Python script.

    > **tip**
    >
    >     import sys
    >     new_path = '/home/emma/user_defined_modules'
    >     if new_path not in sys.path:
    >         sys.path.append(new_path)
    >
    > This method is not very robust, however, because it makes the code
    > less portable (user-dependent path) and because you have to add
    > the directory to your sys.path each time you want to import from a
    > module in this directory.

Packages
--------

A directory that contains many modules is called a *package*. A package
is a module with submodules (which can have submodules themselves,
etc.). A special file called `__init__.py` (which may be empty) tells
Python that the directory is a Python package, from which modules can be
imported.

From Ipython:

Good practices
--------------

-   Use **meaningful** object **names**
-   **Indentation: no choice!**

    > **tip**
    >
    > Indenting is compulsory in Python! Every command block following a
    > colon bears an additional indentation level with respect to the
    > previous line with a colon. One must therefore indent after
    > `def f():` or `while:`. At the end of such logical blocks, one
    > decreases the indentation depth (and re-increases it if a new
    > block is entered, etc.)
    >
    > Strict respect of indentation is the price to pay for getting rid
    > of `{` or `;` characters that delineate logical blocks in
    > other languages. Improper indentation leads to errors such as
    >
    > All this indentation business can be a bit confusing in
    > the beginning. However, with the clear indentation, and in the
    > absence of extra characters, the resulting code is very nice to
    > read compared to other languages.

-   **Indentation depth**: Inside your text editor, you may choose to
    indent with any positive number of spaces (1, 2, 3, 4, ...).
    However, it is considered good practice to **indent with 4 spaces**.
    You may configure your editor to map the `Tab` key to a
    4-space indentation. In Python(x,y), the editor is already
    configured this way.
-   **Style guidelines**

    **Long lines**: you should not write very long lines that span over
    more than (e.g.) 80 characters. Long lines can be broken with the
    `\` character :

        >>> long_line = "Here is a very very long line \
        ... that we break in two parts."

    **Spaces**

    Write well-spaced code: put whitespaces after commas, around
    arithmetic operators, etc.:

        >>> a = 1 # yes
        >>> a=1 # too cramped

    A certain number of rules for writing "beautiful" code (and more
    importantly using the same conventions as anybody else!) are given
    in the [Style Guide for Python
    Code](https://www.python.org/dev/peps/pep-0008).

****Quick read****

If you want to do a first quick pass through the Scipy lectures to learn
the ecosystem, you can directly skip to the next chapter: numpy.

The remainder of this chapter is not necessary to follow the rest of the
intro part. But be sure to come back and finish this chapter later.
