# 1. Higher Order Functions
# A higher order function (HOF) is a function that manipulates other functions by taking in functions as arguments, returning a function, or both. 
# HOFs are powerful abstraction tools that allow us to express certain general patterns as named concepts in our programs. 

# A Note on Lambda Expressions
# A lambda expression evaluates to a function, called a lambda function. 
# A lambda expression by itself evaluates to a function but does not bind it to a name. 
# Also note that the return expression of this function is not evaluated until the lambda is called. 
# Unlike def statement, lambda expressions can be used as an operator or an operand to a call expression. 

# Currying
# One important application of HOFs is converting a function that takes multiple arguments into a chain of functions that each take a single argument. This is known as currying. 

# Questions
# 1.1 Write a function that takes in a function cond and a number n and prints numbers from 1 to n where calling cond on that number returns True. 
def keep_ints(cond, n):
    """Print out all integers 1...i...n where cond(i) is true

    >>> def is_even(x):
    ...     # Even numbers have reaminder 0 when divided by 2.
    ...     return x % 2 == 0
    ...
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i <=n : 
        if cond(i):
            print(i)
        i += 1

# 1.2 Tutorial: Write a function similar to keep_ints like before, but now it takes in a number n and returns a function that has one parameter cond. 
# The returned function prints out numbers from 1 to n where calling cond on that number return True. 
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 1...i...n where calling cond(i) return True. 

    >>> def is_even(x):
    ...     # Even numbers have reaminder 0 when divided by 2.
    ...     return x % 2 == 0
    ...
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def keeper(cond):
        i = 1
        while i <=n: 
            if cond(i):
                print(i)
            i += 1
    return keeper


# HOFs in Environment Diagrams
# Recall that an environment diagram keeps track of all the variables that have been defined and the values they are bound to. 
# However, values are not necessarily only integers and strings. 
# Environment diagrams can model more complex programs that utilize higher order functions.

# The parent of any function (including lambdas) is always the frame in which the function is defined. 

# 1.4 Write curry2 as a lambda function.
curry2 = lambda h: lambda x: lambda y: h(x, y)

# Self Reference
# Self-reference refers to a particular design of HOF, where a function eventually returns itself. 
# In particular, a self-referencing function will not return a function call, but rather the function object itself. 

def print_all(x):
    print(x)
    return print_all

# Self-referencing functions will often times employ helper function that reference the outer function
def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum

# This differens from recursion because typically each new call retruns a new function rather than a functional call. 

# Questions
# 1.7 Write a function print_delayed delays printing its argument until the next function call. print_delayed takes in an argument x and returns a new function delay_print. 
# When delay_print is called, it prints out x and returns another delay_print.

def print_delayed(x):
    """Return a new function. This new function, when called, will print out x and return another function with the same behaviour. 
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed> 
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print


# 1.8 Tutorial: Write a function print_n that can take in an integer n and returns a repeatable print function that can print the next n parameters. 
# After the nth parameter, it just prints "done"
def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first 
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n <= 0: 
            print("done")
        else: 
            print(x)
        return print_n(n-1)
    return inner_print