Advanced operations
===================

Polynomials
-----------

Numpy also contains polynomials in different bases:

For example, $3x^2 + 2x - 1$:

    >>> p = np.poly1d([3, 2, -1])
    >>> p(0)
    -1
    >>> p.roots
    array([-1.        ,  0.33333333])
    >>> p.order
    2

    >>> x = np.linspace(0, 1, 20)
    >>> y = np.cos(x) + 0.3*np.random.rand(20)
    >>> p = np.poly1d(np.polyfit(x, y, 3))

    >>> t = np.linspace(0, 1, 200)
    >>> plt.plot(x, y, 'o', t, p(t), '-')   # doctest: +ELLIPSIS
    [<matplotlib.lines.Line2D object at ...>, <matplotlib.lines.Line2D object at ...>]

See
<http://docs.scipy.org/doc/numpy/reference/routines.polynomials.poly1d.html>
for more.

### More polynomials (with more bases)

Numpy also has a more sophisticated polynomial interface, which supports
e.g. the Chebyshev basis.

$3x^2 + 2x - 1$:

    >>> p = np.polynomial.Polynomial([-1, 2, 3]) # coefs in different order!
    >>> p(0)
    -1.0
    >>> p.roots()
    array([-1.        ,  0.33333333])
    >>> p.degree()  # In general polynomials do not always expose 'order'
    2

Example using polynomials in Chebyshev basis, for polynomials in range
`[-1, 1]`:

    >>> x = np.linspace(-1, 1, 2000)
    >>> y = np.cos(x) + 0.3*np.random.rand(2000)
    >>> p = np.polynomial.Chebyshev.fit(x, y, 90)

    >>> t = np.linspace(-1, 1, 200)
    >>> plt.plot(x, y, 'r.')   # doctest: +ELLIPSIS
    [<matplotlib.lines.Line2D object at ...>]
    >>> plt.plot(t, p(t), 'k-', lw=3)   # doctest: +ELLIPSIS
    [<matplotlib.lines.Line2D object at ...>]

The Chebyshev polynomials have some advantages in interpolation.

Loading data files
------------------

### Text files

Example: populations.txt &lt;../../data/populations.txt&gt;:

    >>> data = np.loadtxt('data/populations.txt')
    >>> data    # doctest: +ELLIPSIS
    array([[  1900.,  30000.,   4000.,  48300.],
           [  1901.,  47200.,   6100.,  48200.],
           [  1902.,  70200.,   9800.,  41500.],
    ...

    >>> np.savetxt('pop2.txt', data)
    >>> data2 = np.loadtxt('pop2.txt')

> **note**
>
> If you have a complicated text file, what you can try are:
>
> -   `np.genfromtxt`
> -   Using Python's I/O functions and e.g. regexps for parsing (Python
>     is quite well suited for this)

**Reminder: Navigating the filesystem with IPython**

### Images

Using Matplotlib:

    >>> img = plt.imread('data/elephant.png')
    >>> img.shape, img.dtype
    ((200, 300, 3), dtype('float32'))
    >>> plt.imshow(img)     # doctest: +ELLIPSIS
    <matplotlib.image.AxesImage object at ...>
    >>> plt.savefig('plot.png')

    >>> plt.imsave('red_elephant', img[:,:,0], cmap=plt.cm.gray)

This saved only one channel (of RGB):

    >>> plt.imshow(plt.imread('red_elephant.png'))  # doctest: +ELLIPSIS
    <matplotlib.image.AxesImage object at ...>

Other libraries:

    >>> from scipy.misc import imsave
    >>> imsave('tiny_elephant.png', img[::6,::6])
    >>> plt.imshow(plt.imread('tiny_elephant.png'), interpolation='nearest')  # doctest: +ELLIPSIS
    <matplotlib.image.AxesImage object at ...>

### Numpy's own format

Numpy has its own binary format, not portable but with efficient I/O:

    >>> data = np.ones((3, 3))
    >>> np.save('pop.npy', data)
    >>> data3 = np.load('pop.npy')

### Well-known (& more obscure) file formats

-   HDF5: [h5py](http://www.h5py.org/),
    [PyTables](http://www.pytables.org)
-   NetCDF: `scipy.io.netcdf_file`,
    [netcdf4-python](http://code.google.com/p/netcdf4-python/), ...
-   Matlab: `scipy.io.loadmat`, `scipy.io.savemat`
-   MatrixMarket: `scipy.io.mmread`, `scipy.io.mmwrite`
-   IDL: `scipy.io.readsav`

... if somebody uses it, there's probably also a Python library for it.

**Exercise: Text data files**

Write a Python script that loads data from populations.txt
&lt;../../data/populations.txt&gt;:: and drop the last column and the
first 5 rows. Save the smaller dataset to `pop2.txt`.

**Numpy internals**

If you are interested in the Numpy internals, there is a good discussion
in advanced\_numpy.
