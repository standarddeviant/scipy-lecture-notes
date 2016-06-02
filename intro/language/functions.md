Defining functions
==================

Function definition
-------------------

> **warning**
>
> Function blocks must be indented as other control-flow blocks.

Return statement
----------------

Functions can *optionally* return values.

> **note**
>
> By default, functions return `None`.

> **note**
>
> Note the syntax to define a function:
>
> -   the `def` keyword;
> -   is followed by the function's **name**, then
> -   the arguments of the function are given between parentheses
>     followed by a colon.
> -   the function body;
> -   and `return object` for optionally returning values.

Parameters
----------

Mandatory parameters (positional arguments)

Optional parameters (keyword or named arguments)

Keyword arguments allow you to specify *default values*.

> **warning**
>
> Default values are evaluated when the function is defined, not when it
> is called. This can be problematic when using mutable types (e.g.
> dictionary or list) and modifying them in the function body, since the
> modifications will be persistent across invocations of the function.
>
> Using an immutable type in a keyword argument:
>
> Using an mutable type in a keyword argument (and modifying it inside
> the function body):

> **tip**
>
> More involved example implementing python's slicing:
>
> The order of the keyword arguments does not matter:
>
> but it is good practice to use the same ordering as the function's
> definition.

*Keyword arguments* are a very convenient feature for defining functions
with a variable number of arguments, especially when default values are
to be used in most calls to the function.

Passing by value
----------------

> **tip**
>
> Can you modify the value of a variable inside a function? Most
> languages (C, Java, ...) distinguish "passing by value" and "passing
> by reference". In Python, such a distinction is somewhat artificial,
> and it is a bit subtle whether your variables are going to be modified
> or not. Fortunately, there exist clear rules.
>
> Parameters to functions are references to objects, which are passed by
> value. When you pass a variable to a function, python passes the
> reference to the object to which the variable refers (the **value**).
> Not the variable itself.

If the **value** passed in a function is immutable, the function does
not modify the caller's variable. If the **value** is mutable, the
function may modify the caller's variable in-place:

    >>> def try_to_modify(x, y, z):
    ...     x = 23
    ...     y.append(42)
    ...     z = [99] # new reference
    ...     print(x)
    ...     print(y)
    ...     print(z)
    ...
    >>> a = 77    # immutable variable
    >>> b = [99]  # mutable variable
    >>> c = [28]
    >>> try_to_modify(a, b, c)
    23
    [99, 42]
    [99]
    >>> print(a)
    77
    >>> print(b)
    [99, 42]
    >>> print(c)
    [28]

Functions have a local variable table called a *local namespace*.

The variable `x` only exists within the function `try_to_modify`.

Global variables
----------------

Variables declared outside the function can be referenced within the
function:

But these "global" variables cannot be modified within the function,
unless declared **global** in the function.

This doesn't work:

This works:

Variable number of parameters
-----------------------------

Special forms of parameters:

:   -   `*args`: any number of positional arguments packed into a tuple
    -   `**kwargs`: any number of keyword arguments packed into a
        dictionary

Docstrings
----------

Documentation about what the function does and its parameters. General
convention:

> **note**
>
> **Docstring guidelines**
>
> For the sake of standardization, the [Docstring
> Conventions](https://www.python.org/dev/peps/pep-0257) webpage
> documents the semantics and conventions associated with Python
> docstrings.
>
> Also, the Numpy and Scipy modules have defined a precise standard for
> documenting scientific functions, that you may want to follow for your
> own functions, with a `Parameters` section, an `Examples` section,
> etc. See
> <http://projects.scipy.org/numpy/wiki/CodingStyleGuidelines#docstring-standard>
> and <http://projects.scipy.org/numpy/browser/trunk/doc/example.py#L37>

Functions are objects
---------------------

Functions are first-class objects, which means they can be:

:   -   assigned to a variable
    -   an item in a list (or any collection)
    -   passed as an argument to another function.

Methods
-------

Methods are functions attached to objects. You've seen these in our
examples on *lists*, *dictionaries*, *strings*, etc...

Exercises
---------

**Exercise: Fibonacci sequence**

Write a function that displays the `n` first terms of the Fibonacci
sequence, defined by:

-   `u_0 = 1; u_1 = 1`
-   `u_(n+2) = u_(n+1) + u_n`

**Exercise: Quicksort**

Implement the quicksort algorithm, as defined by wikipedia
