Basic Python for data processing
================================

The Python language includes a command "shell," which makes it extremely easy
for experimenting with raw data, testing ideas, and inspecting output.


## Python data types

The two primitive _types_ of data we will focus on are numbers and text.
In programming languages, text is referred to as _strings_.

The shell interpreter can take numbers and strings as direct input. Numbers
also obey arithmetic operations, like a simple calculator.

- _variable assignment_ in Python uses equal operator.
- Examples of integer, float, literal and expression assignments.
- Examples of string literal assignment.

Python doesn't care whether you use single or double quotes in expressions.
They just have to be symmetric.

- Examples of simple quote escaping: `'this is a "quoted" string'`.

The `type` of a variable is determined by assignment.
Python is a _dynamic language_: the type of a variable can change by reassignment.

This makes Python flexible and easy for prototyping. It is also prone to mistakes,
and can make things hard to debug.

- Introduce the `type` operator.
- Examples of up-casting in expressions: `int` vs `float`.
- Examples of `TypeError`, eg, with `float` and `str`.


## Python `list` type

A variable of a primitive type (like `int`, `float`, `str`) holds only one value.
An `list` is a _compound type_: a single list holds many values. (Like an array
in Java.)

- Examples of list literals
- Example of list indexing.
- Example of out-of-range errors.
- Introduce the `len` operator.

A useful Python function is `range`, which returns a list of integers of
specified length:

### Experimenting with synthetic data.

Let's import a function from a module to generate random numbers:

    >>> from random import random
    >>> r = random()  # the function takes no arguments
    >>> type(r)
    <type 'float'>

    >>> rs = [random() for i in range(12)]
    >>> type(rs)
    <type 'list'>

    >>> [5 * x for x in rs]
    ...
    >>> [int(5 * x) for x in rs]
    ...

### Questions

1. How would you create a list of 100 random numbers between 0 and 10?
2. How would you create a list of random numbers between 5 and 15?
3. What about a list of random integers between 5 and 15? Or 5 and 15 inclusive?

## Objects, as in _object oriented_

There is a lot of jargon in computer science. It's particularly evident when
discussing object oriented programming languages like Java. And Python.

The "signature" (or _type_) of an object includes a list of functions which
operate on that object: they affect the state of the object, or produce output
about the state, without actually changing it. However instead of functions
they're called _methods_.

Like Java, Python uses the dot-notation to apply methods:

    >>> Object.method(arg1, arg2, ...)


## Python `file` type

The Python function `open` takes 2 arguments and returns a _file object_.
The arguments are the file name (which can include path information), and
the _mode_.

Modes we use for text files are _read_, _write_, and _append_.

### Read methods

If the mode argument is omitted, the default is for reading.

A file object in read mode has two important methods:
1. `read` -- returns the entire file as a single string.
2. `readlines` -- returns the file as a list of strings.

    >>> fobj = open('data/ZenOfPython.txt')
    >>> zop = fobj.read()
    >>> fobj.close()
    ...
    >>> lines = fobj.readlines()

### Write methods

The `write` method takes one argument: the string written (or appended) to the
file on disk.

    >>> fobj = open('testfile.txt', 'w')
    >>> fobj.write('This will be written to disk\n')
    >>> fobj.close()

    >>> fobj = open('testfile.txt', 'a')
    >>> fobj.write('This will be appended to the file\n')
    >>> fobj.close()


## String methods

Although we introduced strings as "primitive" types, that is not really accurate.
In Python, a string is an object with lots of powerful methods.

- Examples of `split` method.
- Examples of `strip` method.
- Examples of `find` and `replace` methods.

See [http://docs.python.org/2/library/stdtypes.html#string-methods](http://docs.python.org/2/library/stdtypes.html#string-methods)
for many more.


## Example file processing program

The _for-loop_ and the _if-condition_ are constructs common to all modern
programming languages (Python, Java, C++). Where Java uses curly braces to
denote a code block for a for-loop, Python uses a colon and indentation...

    f_in = open('data/ZenOfPython.txt')
    for line in f_in.readlines():
        words = line.split(' ')
        print words[0]

    f_in.close()

### Questions

1. What's going on in the second and third lines of output of this program?
2. Modify the program to output the number of words in each line.
3. Modify the program to print only lines which contain "is".
4. What's going on with the spacing in (3), and how can you fix it?


## Python `dict` type

A dictionary, or `dict`, is a special type of compound type.
Whereas a list can hold many data item, each item can only be accessed by
its numerical index. A dictionary uses any data -- not just numbers --
for the indices. Some languages call this an "associative array," because
it associates one data item to another.

- Examples of list literals.
- Examples of list indexing.
- Examples of `KeyError`, like `IndexError`.
- Example of `get` and `setdefault` methods.
- Explanation of _keys_ versus _values_.
- Eamples of `keys`, `values`, `items` methods.


Data Science demo with NYC OpenData
-----------------------------------

New York City government continually publishes data sets related to all facets of
city affairs: education, the economy, transportation, public safety, environmental
statistics, an many others.

These are hosted at [data.cityofnewyork.us/](https://data.cityofnewyork.us/)
with a nice suite of tools for searching, filtering, and even visualizing the data sets.
Even with all of these resources efforts, the data sets are very heterogeneous,
often messy, and don't always play well with the online exploration tools.

Once you get your hands on a data set, you've still got to understand what's in it.
**Data exploration** is an iterative process: getting to understand a data set in
concrete, bite-sized steps. It can be frustrating. Sometimes you may have to back up
several steps and start again in a new direction. Sometimes you just reach the conclusion
that the data set lends no new insight into what you thought it might. Bummer.

There are _plenty_ of Python libraries and tools for drilling into data. These are not
built in functions, but packages accessible using Python's `import` command, and
they have volumes of documentation online. Instead of taking this approach,
we will step through some illustrations of concepts in the first part of this
workshop using tools in the `pytools` module of this repository.

A couple data sets for exploration:

- [Manhattan condo price data](https://data.cityofnewyork.us/Housing-Development/DOF-Condominium-comparable-rental-income-Manhattan/ikqj-pyhc)
- [City community gardens data](https://data.cityofnewyork.us/Environment/NYC-Greenthumb-Community-Gardens/ajxm-kzmj)

And the concepts we want to illustrate are

- loading the data set as a Python list of _rows_,
- extracting the field names -- ie, column headers -- from a CSV file,
- extracting one or more columns from a data set,
- filtering and transforming a single column,
- saving the transformed data set for further processing.
