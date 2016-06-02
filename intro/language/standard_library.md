Standard Library
================

> **note**
>
> Reference document for this section:
>
> -   The Python Standard Library documentation:
>     <https://docs.python.org/library/index.html>
> -   Python Essential Reference, David Beazley, Addison-Wesley
>     Professional

`os` module: operating system functionality
-------------------------------------------

*"A portable way of using operating system dependent functionality."*

### Directory and file manipulation

Current directory:

List a directory:

Make a directory:

Rename the directory:

Delete a file:

### `os.path`: path manipulations

`os.path` provides common operations on pathnames.

### Running an external command

> **note**
>
> Alternative to `os.system`
>
> A noteworthy alternative to `os.system` is the [sh
> module](http://amoffat.github.com/sh/). Which provides much more
> convenient ways to obtain the output, error stream and exit code of
> the external command.

### Walking a directory

`os.path.walk` generates a list of filenames in a directory tree.

### Environment variables:

`shutil`: high-level file operations
------------------------------------

The `shutil` provides useful file operations:

> -   `shutil.rmtree`: Recursively delete a directory tree.
> -   `shutil.move`: Recursively move a file or directory to
>     another location.
> -   `shutil.copy`: Copy files or directories.

`glob`: Pattern matching on files
---------------------------------

The `glob` module provides convenient file pattern matching.

Find all files ending in `.txt`:

`sys` module: system-specific information
-----------------------------------------

System-specific information related to the Python interpreter.

-   Which version of python are you running and where is it installed:
-   List of command line arguments passed to a Python script:

`sys.path` is a list of strings that specifies the search path for
modules. Initialized from PYTHONPATH:

`pickle`: easy persistence
--------------------------

Useful to store arbitrary objects to a file. Not safe or fast!

**Exercise**

Write a program to search your `PYTHONPATH` for the module `site.py`.

path\_site
