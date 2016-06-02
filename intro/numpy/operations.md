Numerical operations on arrays
==============================

Elementwise operations
----------------------

### Basic operations

With scalars:

All arithmetic operates elementwise:

These operations are of course much faster than if you did them in pure
python:

> **warning**
>
> **Array multiplication is not matrix multiplication:**

> **note**
>
> **Matrix multiplication:**

****Exercise: Elementwise operations****

-   Try simple arithmetic elementwise operations: add even elements with
    odd elements
-   Time them against their pure python counterparts using `%timeit`.
-   Generate:
    -   `[2**0, 2**1, 2**2, 2**3, 2**4]`
    -   `a_j = 2^(3*j) - j`

### Other operations

**Comparisons:**

> **tip**
>
> Array-wise comparisons:

**Logical operations:**

**Transcendental functions:**

**Shape mismatches**

*Broadcasting?* We'll return to that later &lt;broadcasting&gt;.

**Transposition:**

> **warning**
>
> **The transposition is a view**
>
> As a results, the following code **is wrong** and will **not make a
> matrix symmetric**:
>
>     >>> a += a.T
>
> It will work for small arrays (because of buffering) but fail for
> large one, in unpredictable ways.

> **note**
>
> **Linear algebra**
>
> The sub-module numpy.linalg implements basic linear algebra, such as
> solving linear systems, singular value decomposition, etc. However, it
> is not guaranteed to be compiled using efficient routines, and thus we
> recommend the use of scipy.linalg, as detailed in section
> scipy\_linalg

**Exercise other operations**

-   Look at the help for `np.allclose`. When might this be useful?
-   Look at the help for `np.triu` and `np.tril`.

Basic reductions
----------------

### Computing sums

![image](images/reductions.png)

Sum by rows and by columns:

> **tip**
>
> Same idea in higher dimensions:

### Other reductions

--- works the same way (and take `axis=`)

**Extrema:**

**Logical operations:**

> **note**
>
> Can be used for array comparisons:

**Statistics:**

... and many more (best to learn as you go).

****Exercise: Reductions****

-   Given there is a `sum`, what other function might you expect to see?
-   What is the difference between `sum` and `cumsum`?

**Worked Example: data statistics**

Data in populations.txt &lt;../../data/populations.txt&gt; describes the
populations of hares and lynxes (and carrots) in northern Canada during
20 years.

You can view the data in an editor, or alternatively in IPython (both
shell and notebook):

First, load the data into a Numpy array:

Then plot it:

The mean populations over time:

The sample standard deviations:

Which species has the highest population each year?:

**Worked Example: diffusion using a random walk algorithm**

![image](random_walk.png)

> **tip**
>
> Let us consider a simple 1D random walk process: at each time step a
> walker jumps right or left with equal probability.
>
> We are interested in finding the typical distance from the origin of a
> random walker after `t` left or right jumps? We are going to simulate
> many "walkers" to find this law, and we are going to do so using array
> computing tricks: we are going to create a 2D array with the "stories"
> (each walker has a story) in one direction, and the time in the other:

We randomly choose all the steps 1 or -1 of the walk:

We build the walks by summing steps along the time:

We get the mean in the axis of the stories:

Plot the results:

We find a well-known result in physics: the RMS distance grows as the
square root of the time!

Broadcasting
------------

-   Basic operations on `numpy` arrays (addition, etc.) are elementwise
-   This works on arrays of the same size.

    > **Nevertheless**, It's also possible to do operations on arrays of
    > different\
    > sizes if *Numpy* can transform these arrays so that they all have\
    > the same size: this conversion is called **broadcasting**.

The image below gives an example of broadcasting:

Let's verify:

We have already used broadcasting without knowing it!:

An useful trick:

> **tip**
>
> Broadcasting seems a bit magical, but it is actually quite natural to
> use it when we want to solve a problem whose output data is an array
> with more dimensions than input data.

**Worked Example: Broadcasting**

Let's construct an array of distances (in miles) between cities of Route
66: Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City, Amarillo,
Santa Fe, Albuquerque, Flagstaff and Los Angeles.

![image](images/route66.png)

A lot of grid-based or network-based problems can also use broadcasting.
For instance, if we want to compute the distance from the origin of
points on a 10x10 grid, we can do

Or in color:

**Remark** : the `numpy.ogrid` function allows to directly create
vectors x and y of the previous example, with two "significant
dimensions":

> **tip**
>
> So, `np.ogrid` is very useful as soon as we have to handle
> computations on a grid. On the other hand, `np.mgrid` directly
> provides matrices full of indices for cases where we can't (or don't
> want to) benefit from broadcasting:

Array shape manipulation
------------------------

### Flattening

Higher dimensions: last dimensions ravel out "first".

### Reshaping

The inverse operation to flattening:

Or,

> **warning**
>
> `ndarray.reshape` **may** return a view (cf `help(np.reshape)`)), or
> copy

> **tip**
>
> Beware: reshape may also return a copy!:
>
> To understand this you need to learn more about the memory layout of a
> numpy array.

### Adding a dimension

Indexing with the `np.newaxis` object allows us to add an axis to an
array (you have seen this already above in the broadcasting section):

### Dimension shuffling

Also creates a view:

### Resizing

Size of an array can be changed with `ndarray.resize`:

However, it must not be referred to somewhere else:

****Exercise: Shape manipulations****

-   Look at the docstring for `reshape`, especially the notes section
    which has some more information about copies and views.
-   Use `flatten` as an alternative to `ravel`. What is the difference?
    (Hint: check which one returns a view and which a copy)
-   Experiment with `transpose` for dimension shuffling.

Sorting data
------------

Sorting along an axis:

> **note**
>
> Sorts each row separately!

In-place sort:

Sorting with fancy indexing:

Finding minima and maxima:

****Exercise: Sorting****

-   Try both in-place and out-of-place sorting.
-   Try creating arrays with different dtypes and sorting them.
-   Use `all` or `array_equal` to check the results.
-   Look at `np.random.shuffle` for a way to create sortable
    input quicker.
-   Combine `ravel`, `sort` and `reshape`.
-   Look at the `axis` keyword for `sort` and rewrite the
    previous exercise.

Summary
-------

**What do you need to know to get started?**

-   Know how to create arrays : `array`, `arange`, `ones`, `zeros`.
-   Know the shape of the array with `array.shape`, then use slicing to
    obtain different views of the array: `array[::2]`, etc. Adjust the
    shape of the array using `reshape` or flatten it with `ravel`.
-   Obtain a subset of the elements of an array and/or modify their
    values with masks
-   Know miscellaneous operations on arrays, such as finding the mean or
    max (`array.max()`, `array.mean()`). No need to retain everything,
    but have the reflex to search in the documentation (online docs,
    `help()`, `lookfor()`)!!
-   For advanced use: master the indexing with arrays of integers, as
    well as broadcasting. Know more Numpy functions to handle various
    array operations.

****Quick read****

If you want to do a first quick pass through the Scipy lectures to learn
the ecosystem, you can directly skip to the next chapter: matplotlib.

The remainder of this chapter is not necessary to follow the rest of the
intro part. But be sure to come back and finish this chapter, as well as
to do some more exercices &lt;numpy\_exercises&gt;.
