Basic types
===========

Numerical types
---------------

> **tip**
>
> Python supports the following numerical, scalar types:

Integer

:   

> &gt;&gt;&gt; 1 + 1 2 &gt;&gt;&gt; a = 4 &gt;&gt;&gt; type(a) \#
> doctest: +SKIP &lt;type 'int'&gt;

Floats

:   

> &gt;&gt;&gt; c = 2.1 &gt;&gt;&gt; type(c) \# doctest: +SKIP &lt;type
> 'float'&gt;

Complex

:   

> &gt;&gt;&gt; a = 1.5 + 0.5j &gt;&gt;&gt; a.real 1.5 &gt;&gt;&gt;
> a.imag 0.5 &gt;&gt;&gt; type(1. + 0j) \# doctest: +SKIP &lt;type
> 'complex'&gt;

Booleans

:   

> &gt;&gt;&gt; 3 &gt; 4 False &gt;&gt;&gt; test = (3 &gt; 4)
> &gt;&gt;&gt; test False &gt;&gt;&gt; type(test) \# doctest: +SKIP
> &lt;type 'bool'&gt;

> **tip**
>
> A Python shell can therefore replace your pocket calculator, with the
> basic arithmetic operations `+`, `-`, `*`, `/`, `%` (modulo) natively
> implemented

    >>> 7 * 3.
    21.0
    >>> 2**10
    1024
    >>> 8 % 3
    2

Type conversion (casting):

    >>> float(1)
    1.0

> **warning**
>
> Integer division
>
> In Python 2:
>
>     >>> 3 / 2   # doctest: +SKIP
>     1
>
> In Python 3:
>
>     >>> 3 / 2   # doctest: +SKIP
>     1.5
>
> **To be safe**: use floats:
>
>     >>> 3 / 2.
>     1.5
>
>     >>> a = 3
>     >>> b = 2
>     >>> a / b # In Python 2  # doctest: +SKIP
>     1
>     >>> a / float(b)
>     1.5
>
> **Future behavior**: to always get the behavior of Python3
>
> > &gt;&gt;&gt; from \_\_future\_\_ import division \# doctest: +SKIP
> > &gt;&gt;&gt; 3 / 2 \# doctest: +SKIP 1.5
>
> > **tip**
> >
> > If you explicitly want integer division use `//`:
> >
> >     >>> 3.0 // 2
> >     1.0
> >
> > > **note**
> > >
> > > The behaviour of the division operator has changed in [Python
> > > 3](http://python3porting.com/preparing.html#use-instead-of-when-dividing-integers).

Containers
----------

> **tip**
>
> Python provides many efficient types of containers, in which
> collections of objects can be stored.

### Lists

> **tip**
>
> A list is an ordered collection of objects, that may have different
> types. For example:

    >>> l = ['red', 'blue', 'green', 'black', 'white']
    >>> type(l)     # doctest: +SKIP
    <type 'list'>

Indexing: accessing individual objects contained in the list:

    >>> l[2]
    'green'

Counting from the end with negative indices:

    >>> l[-1]
    'white'
    >>> l[-2]
    'black'

> **warning**
>
> **Indexing starts at 0** (as in C), not at 1 (as in Fortran or
> Matlab)!

Slicing: obtaining sublists of regularly-spaced elements:

    >>> l
    ['red', 'blue', 'green', 'black', 'white']
    >>> l[2:4]
    ['green', 'black']

> **warning**
>
> Note that `l[start:stop]` contains the elements with indices `i` such
> as `start<= i < stop` (`i` ranging from `start` to `stop-1`).
> Therefore, `l[start:stop]` has `(stop - start)` elements.

**Slicing syntax**: `l[start:stop:stride]`

> **tip**
>
> All slicing parameters are optional:
>
>     >>> l
>     ['red', 'blue', 'green', 'black', 'white']
>     >>> l[3:]
>     ['black', 'white']
>     >>> l[:3]
>     ['red', 'blue', 'green']
>     >>> l[::2]
>     ['red', 'green', 'white']

Lists are *mutable* objects and can be modified:

    >>> l[0] = 'yellow'
    >>> l
    ['yellow', 'blue', 'green', 'black', 'white']
    >>> l[2:4] = ['gray', 'purple']
    >>> l
    ['yellow', 'blue', 'gray', 'purple', 'white']

> **note**
>
> The elements of a list may have different types:
>
>     >>> l = [3, -200, 'hello']
>     >>> l
>     [3, -200, 'hello']
>     >>> l[1], l[2]
>     (-200, 'hello')
>
> > **tip**
> >
> > For collections of numerical data that all have the same type, it is
> > often **more efficient** to use the `array` type provided by the
> > `numpy` module. A NumPy array is a chunk of memory containing
> > fixed-sized items. With NumPy arrays, operations on elements can be
> > faster because elements are regularly spaced in memory and more
> > operations are performed through specialized C functions instead of
> > Python loops.

> **tip**
>
> Python offers a large panel of functions to modify lists, or query
> them. Here are a few examples; for more details, see
> <https://docs.python.org/tutorial/datastructures.html#more-on-lists>

Add and remove elements:

    >>> L = ['red', 'blue', 'green', 'black', 'white']
    >>> L.append('pink')
    >>> L
    ['red', 'blue', 'green', 'black', 'white', 'pink']
    >>> L.pop() # removes and returns the last item
    'pink'
    >>> L
    ['red', 'blue', 'green', 'black', 'white']
    >>> L.extend(['pink', 'purple']) # extend L, in-place
    >>> L
    ['red', 'blue', 'green', 'black', 'white', 'pink', 'purple']
    >>> L = L[:-2]
    >>> L
    ['red', 'blue', 'green', 'black', 'white']

Reverse:

    >>> r = L[::-1]
    >>> r
    ['white', 'black', 'green', 'blue', 'red']
    >>> r2 = list(L)
    >>> r2
    ['red', 'blue', 'green', 'black', 'white']
    >>> r2.reverse() # in-place
    >>> r2
    ['white', 'black', 'green', 'blue', 'red']

Concatenate and repeat lists:

    >>> r + L
    ['white', 'black', 'green', 'blue', 'red', 'red', 'blue', 'green', 'black', 'white']
    >>> r * 2
    ['white', 'black', 'green', 'blue', 'red', 'white', 'black', 'green', 'blue', 'red']

> **tip**
>
> Sort:
>
>     >>> sorted(r) # new object
>     ['black', 'blue', 'green', 'red', 'white']
>     >>> r
>     ['white', 'black', 'green', 'blue', 'red']
>     >>> r.sort()  # in-place
>     >>> r
>     ['black', 'blue', 'green', 'red', 'white']

****Methods and Object-Oriented Programming****

The notation `r.method()` (e.g. `r.append(3)` and `L.pop()`) is our
first example of object-oriented programming (OOP). Being a `list`, the
object r owns the *method* function that is called using the notation
**.**. No further knowledge of OOP than understanding the notation **.**
is necessary for going through this tutorial.

****Discovering methods:****

Reminder: in Ipython: tab-completion (press tab)

### Strings

Different string syntaxes (simple, double or triple quotes):

    s = 'Hello, how are you?'
    s = "Hi, what's up"
    s = '''Hello,                 # tripling the quotes allows the
           how are you'''         # the string to span more than one line
    s = """Hi,
    what's up?"""

The newline character is `\n`, and the tab character is `\t`.

> **tip**
>
> Strings are collections like lists. Hence they can be indexed and
> sliced, using the same syntax and rules.

Indexing:

    >>> a = "hello"
    >>> a[0]
    'h'
    >>> a[1]
    'e'
    >>> a[-1]
    'o'

> **tip**
>
> (Remember that negative indices correspond to counting from the right
> end.)

Slicing:

    >>> a = "hello, world!"
    >>> a[3:6] # 3rd to 6th (excluded) elements: elements 3, 4, 5
    'lo,'
    >>> a[2:10:2] # Syntax: a[start:stop:step]
    'lo o'
    >>> a[::3] # every three characters, from beginning to end
    'hl r!'

> **tip**
>
> Accents and special characters can also be handled in Unicode strings
> (see
> <https://docs.python.org/tutorial/introduction.html#unicode-strings>).

A string is an **immutable object** and it is not possible to modify its
contents. One may however create new strings from the original one.

> **tip**
>
> Strings have many useful methods, such as `a.replace` as seen above.
> Remember the `a.` object-oriented notation and use tab completion or
> `help(str)` to search for new methods.

String formatting:

    >>> 'An integer: %i; a float: %f; another string: %s' % (1, 0.1, 'string')
    'An integer: 1; a float: 0.100000; another string: string'

    >>> i = 102
    >>> filename = 'processing_of_dataset_%d.txt' % i
    >>> filename
    'processing_of_dataset_102.txt'

### Dictionaries

> **tip**
>
> A dictionary is basically an efficient table that **maps keys to
> values**. It is an **unordered** container

    >>> tel = {'emmanuelle': 5752, 'sebastian': 5578}
    >>> tel['francis'] = 5915
    >>> tel     # doctest: +SKIP
    {'sebastian': 5578, 'francis': 5915, 'emmanuelle': 5752}
    >>> tel['sebastian']
    5578
    >>> tel.keys()   # doctest: +SKIP
    ['sebastian', 'francis', 'emmanuelle']
    >>> tel.values()   # doctest: +SKIP
    [5578, 5915, 5752]
    >>> 'francis' in tel
    True

> **tip**
>
> It can be used to conveniently store and retrieve values associated
> with a name (a string for a date, a name, etc.). See
> <https://docs.python.org/tutorial/datastructures.html#dictionaries>
> for more information.
>
> A dictionary can have keys (resp. values) with different types:
>
>     >>> d = {'a':1, 'b':2, 3:'hello'}
>     >>> d       # doctest: +SKIP
>     {'a': 1, 3: 'hello', 'b': 2}

### More container types

**Tuples**

Tuples are basically immutable lists. The elements of a tuple are
written between parentheses, or just separated by commas:

    >>> t = 12345, 54321, 'hello!'
    >>> t[0]
    12345
    >>> t
    (12345, 54321, 'hello!')
    >>> u = (0, 2)

**Sets:** unordered, unique items:

    >>> s = set(('a', 'b', 'c', 'a'))
    >>> s    # doctest: +SKIP
    set(['a', 'c', 'b'])
    >>> s.difference(('a', 'b'))    # doctest: +SKIP
    set(['c'])

Assignment operator
-------------------

> **tip**
>
> [Python library
> reference](https://docs.python.org/reference/simple_stmts.html#assignment-statements)
> says:
>
> > Assignment statements are used to (re)bind names to values and to
> > modify attributes or items of mutable objects.
>
> In short, it works as follows (simple assignment):
>
> 1.  an expression on the right hand side is evaluated, the
>     corresponding object is created/obtained
> 2.  a **name** on the left hand side is assigned, or bound, to
>     the r.h.s. object

Things to note:

-   a single object can have several names bound to it:

-   to change a list *in place*, use indexing/slices:

-   the key concept here is **mutable vs. immutable**

    > -   mutable objects can be changed in place
    > -   immutable objects cannot be modified once created


