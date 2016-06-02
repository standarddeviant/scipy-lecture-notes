Exception handling in Python
============================

It is likely that you have raised Exceptions if you have typed all the
previous commands of the tutorial. For example, you may have raised an
exception if you entered a command with a typo.

Exceptions are raised by different kinds of errors arising when
executing Python code. In your own code, you may also catch errors, or
define custom error types. You may want to look at the descriptions of
the [the built-in
Exceptions](https://docs.python.org/2/library/exceptions.html) when
looking for the right exception type.

Exceptions
----------

Exceptions are raised by errors in Python:

As you can see, there are **different types** of exceptions for
different errors.

Catching exceptions
-------------------

### try/except

### try/finally

Important for resource management (e.g. closing a file)

### Easier to ask for forgiveness than for permission

Raising exceptions
------------------

-   Capturing and reraising an exception:
-   Exceptions to pass messages between parts of the code:

Use exceptions to notify certain conditions are met (e.g. StopIteration)
or not (e.g. custom error raising)
