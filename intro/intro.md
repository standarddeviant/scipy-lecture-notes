Scientific computing with tools and workflow
============================================

**Authors**: *Fernando Perez, Emmanuelle Gouillart, Gaël Varoquaux,
Valentin Haenel*

Why Python?
-----------

### The scientist's needs

-   Get data (simulation, experiment control),
-   Manipulate and process data,
-   Visualize results (to understand what we are doing!),
-   Communicate results: produce figures for reports or publications,
    write presentations.

### Specifications

-   Rich collection of already existing **bricks** corresponding to
    classical numerical methods or basic actions: we don't want to
    re-program the plotting of a curve, a Fourier transform or a
    fitting algorithm. Don't reinvent the wheel!
-   Easy to learn: computer science is neither our job nor
    our education. We want to be able to draw a curve, smooth a signal,
    do a Fourier transform in a few minutes.
-   Easy communication with collaborators, students, customers, to make
    the code live within a lab or a company: the code should be as
    readable as a book. Thus, the language should contain as few syntax
    symbols or unneeded routines as possible that would divert the
    reader from the mathematical or scientific understanding of
    the code.
-   Efficient code that executes quickly... but needless to say that a
    very fast code becomes useless if we spend too much time writing it.
    So, we need both a quick development time and a quick
    execution time.
-   A single environment/language for everything, if possible, to avoid
    learning a new software for each new problem.

### Existing solutions

Which solutions do scientists use to work?

**Compiled languages: C, C++, Fortran, etc.**

-   Advantages:
    -   Very fast. Very optimized compilers. For heavy computations,
        it's difficult to outperform these languages.
    -   Some very optimized scientific libraries have been written for
        these languages. Example: BLAS (vector/matrix operations)
-   Drawbacks:
    -   Painful usage: no interactivity during development, mandatory
        compilation steps, verbose syntax (&, ::, }}, ; etc.), manual
        memory management (tricky in C). These are **difficult
        languages** for non computer scientists.

**Scripting languages: Matlab**

-   Advantages:
    -   Very rich collection of libraries with numerous algorithms, for
        many different domains. Fast execution because these libraries
        are often written in a compiled language.
    -   Pleasant development environment: comprehensive and well
        organized help, integrated editor, etc.
    -   Commercial support is available.
-   Drawbacks:
    -   Base language is quite poor and can become restrictive for
        advanced users.
    -   Not free.

**Other scripting languages: Scilab, Octave, Igor, R, IDL, etc.**

-   Advantages:
    -   Open-source, free, or at least cheaper than Matlab.
    -   Some features can be very advanced (statistics in R, figures in
        Igor, etc.)
-   Drawbacks:
    -   Fewer available algorithms than in Matlab, and the language is
        not more advanced.
    -   Some software are dedicated to one domain. Ex: Gnuplot or
        xmgrace to draw curves. These programs are very powerful, but
        they are restricted to a single type of usage, such as plotting.

**What about Python?**

-   Advantages:
    -   Very rich scientific computing libraries (a bit less than
        Matlab, though)
    -   Well thought out language, allowing to write very readable and
        well structured code: we "code what we think".
    -   Many libraries for other tasks than scientific computing (web
        server management, serial port access, etc.)
    -   Free and open-source software, widely spread, with a
        vibrant community.
-   Drawbacks:
    -   less pleasant development environment than, for example, Matlab.
        (More geek-oriented).
    -   Not all the algorithms that can be found in more specialized
        software or toolboxes.

Scientific Python building blocks
---------------------------------

Unlike Matlab, Scilab or R, Python does not come with a pre-bundled set
of modules for scientific computing. Below are the basic building blocks
that can be combined to obtain a scientific computing environment:

-   **Python**, a generic and modern computing language

    > -   Python language: data types (`string`, `int`), flow control,
    >     data collections (lists, dictionaries), patterns, etc.
    > -   Modules of the standard library.
    > -   A large number of specialized modules or applications written
    >     in Python: web protocols, web framework, etc. ... and
    >     scientific computing.
    > -   Development tools (automatic testing,
    >     documentation generation)

    ![image](snapshot_ipython.png)

-   **IPython**, an advanced **Python shell** <http://ipython.org/>
-   **Numpy** : provides powerful **numerical arrays** objects, and
    routines to manipulate them. <http://www.numpy.org/>

<!-- -->

-   **Scipy** : high-level data processing routines. Optimization,
    regression, interpolation, etc <http://www.scipy.org/>

    ![image](random_c.jpg)

-   **Matplotlib** : 2-D visualization, "publication-ready" plots
    <http://matplotlib.org/>

    |clear-floats|

    ![image](example_surface_from_irregular_data.jpg)

-   **Mayavi** : 3-D visualization
    <http://code.enthought.com/projects/mayavi/>

    |clear-floats|

The interactive workflow: IPython and a text editor
---------------------------------------------------

**Interactive work to test and understand algorithms:** In this section,
we describe an interactive workflow with [IPython](http://ipython.org)
that is handy to explore and understand algorithms.

Python is a general-purpose language. As such, there is not one blessed
environment to work in, and not only one way of using it. Although this
makes it harder for beginners to find their way, it makes it possible
for Python to be used to write programs, in web servers, or embedded
devices.

**Reference document for this section:**

**IPython user manual:** <http://ipython.org/ipython-doc/dev/index.html>

### Command line interaction

Start \`ipython\`:

Getting help by using the **?** operator after an object:

### Elaboration of the algorithm in an editor

Create a file my\_file.py in a text editor. Under EPD (Enthought Python
Distribution), you can use Scite, available from the start menu. Under
Python(x,y), you can use Spyder. Under Ubuntu, if you don't already have
your favorite editor, we would advise installing Stani's Python editor.
In the file, add the following lines:

    s = 'Hello world'
    print(s)

Now, you can run it in IPython and explore the resulting variables:

****From a script to functions****

While it is tempting to work only with scripts, that is a file full of
instructions following each other, do plan to progressively evolve the
script to a set of functions:

-   A script is not reusable, functions are.
-   Thinking in terms of functions helps breaking the problem in
    small blocks.

### IPython Tips and Tricks

The IPython user manual contains a wealth of information about using
IPython, but to get you started we want to give you a quick introduction
to four useful features: *history*, *magic functions*, *aliases* and
*tab completion*.

Like a UNIX shell, IPython supports command history. Type *up* and
*down* to navigate previously typed commands:

IPython supports so called *magic* functions by prefixing a command with
the `%` character. For example, the `run` and `whos` functions from the
previous section are magic functions. Note that, the setting
`automagic`, which is enabled by default, allows you to omit the
preceding `%` sign. Thus, you can just type the magic function and it
will work.

Other useful magic functions are:

-   `%cd` to change the current directory.
-   `%timeit` allows you to time the execution of short snippets using
    the `timeit` module from the standard library:
-   `%cpaste` allows you to paste code, especially code from websites
    which has been prefixed with the standard Python prompt (e.g. `>>>`)
    or with an ipython prompt, (e.g. `in [3]`):
-   `%debug` allows you to enter post-mortem debugging. That is to say,
    if the code you try to execute, raises an exception, using `%debug`
    will enter the debugger at the point where the exception was thrown.

****IPython help****

-   The built-in IPython cheat-sheet is accessible via the `%quickref`
    magic function.
-   A list of all available magic functions is shown when typing
    `%magic`.

Furthermore IPython ships with various *aliases* which emulate common
UNIX command line tools such as `ls` to list files, `cp` to copy files
and `rm` to remove files. A list of aliases is shown when typing
`alias`:

Lastly, we would like to mention the *tab completion* feature, whose
description we cite directly from the IPython manual:

*Tab completion, especially for attributes, is a convenient way to
explore the structure of any object you’re dealing with. Simply type
object\_name.&lt;TAB&gt; to view the object’s attributes. Besides Python
objects and keywords, tab completion also works on file and directory
names.*
