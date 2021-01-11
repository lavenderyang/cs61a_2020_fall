def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    # for i in it: 
    #     yield i * multiplier
    yield from map(lambda x: multiplier * x, it)

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    if n == 1: 
        pass
    elif n % 2 == 0: 
        yield from hailstone(n // 2)
    else: 
        yield from hailstone(n * 3 + 1)


def generator(): 
    print("Starting here")
    i = 0
    while i < 6: 
        print("Before yield")
        yield i
        print("After yield ")
        i += 1

# def trap(s, k): 
#     """Return a generator that yields the first K values in iterable S, 
#     but raises a ValueError exception if any more values are requested. 

#     >>> t = trap([3, 2, 1], 2)
#     >>> next(t)
#     3
#     >>> next(t) 
#     2
#     >>> next(t)
#     ValueError
#     >>> list(trap(range(5), 5))
#     ValueError
#     """
#     assert len(s) >= k
#     "*** YOUR CODE HERE ***"
#     t = iter(s)
#     i = 0
#     while i < k:
#         yield next(t)
#         i += 1
#     raise ValueError()

# def repeated(t, k):
#     """Return the first value in iterator T that appears K times in a row. 

#     >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
#     >>> repeated(trap(s, 7), 2)
#     4
#     >>> repeated(trap(s, 10), 3)
#     5
#     >>> print(repeated([4, None, None, None], 3))
#     None
#     """
#     assert k > 1
#     "*** YOUR CODE HERE ***" 
#     count = 0
#     first = True
#     for item in t:  
#         if first: 
#             first, previous = False, item
#             count += 1
#         elif item == previous: 
#             count += 1
#         else: 
#             previous = item
#             count = 0
#         if count == k: 
#             return item 