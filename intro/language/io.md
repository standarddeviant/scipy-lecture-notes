Input and Output
================

To be exhaustive, here are some information about input and output in
Python. Since we will use the Numpy methods to read and write files,
**you may skip this chapter at first reading**.

We write or read **strings** to/from files (other types must be
converted to strings). To write in a file:

    >>> f = open('workfile', 'w') # opens the workfile file
    >>> type(f)    # doctest: +SKIP 
    <type 'file'>
    >>> f.write('This is a test \nand another test')   # doctest: +SKIP 
    >>> f.close()

To read from a file

Iterating over a file
---------------------

### File modes

-   Read-only: `r`
-   Write-only: `w`
    -   Note: Create a new file or *overwrite* existing file.
-   Append a file: `a`
-   Read and Write: `r+`
-   Binary mode: `b`
    -   Note: Use for binary files, especially on Windows.

