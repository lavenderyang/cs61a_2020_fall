# Nonlocal
# Until now, you've been able to access names in parent frames, but you have not been able to modify them. 
# The nonlocal keyword can be used to modify a binding in a parent frame. 

def stepper(num):
    def step(): 
        nonlocal num    # declares num as a nonlocal name
        num = num + 1   # modifies num in the stepper frame
        return num
    return step

# As illustrated in this example, nonlocal is useful for maintaining state across different calls to the same function. 
# However, there are two important caveats with nonlocal names: 
# A variable declared nonlocal must be defined in a parent frame which is not the global frame
# Names in the current frame cannot be overridden using the nonlocal keyword. This means we cannot have both a local and nonlocal binding with
# the same name in a single frame. 

# Becasue nonlocal lets you modify bindings in parent frames, we call functions that use it mutable functions. 

# Questions 1.1
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n 
    return f


# 2. Mutation
# List mutation. In Python, some objects, such as lists and dictionaries, are mutable, meaning that their contents or state can be changed over the course of program exectuion. 
# Other objects, such as numeric types, tuples and strings, are immutable, meaning they cannot be changed once they are created. 

# A list of useful list mutation methods: 
# 1. append(el): add el to the end of the list, and return None
# 2. extend(lst): Extends the list by concatenating it with lst, and returns None. 
# 3. insert(i, el): Insert el at index (does not replace element but adds a new one), and returns None
# 4. remove(el): Removes the first occurence of el in list, otherwise errors, and return None
# 5. pop(i): Removes and returns the element at index i

# Question 2.2.
def mystery(p, q): 
    p[1].extend(q)
    q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)

# Question 2.3
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for elem in s: 
        key = fn(elem)
        if key in grouped: 
            grouped[key].append(elem)
        else: 
            grouped[key] = [elem]
    return grouped

# Question 2.4
def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s. 
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    counter = 0
    for i in s: 
        if i == x: 
            counter += 1
    for i in range(counter): 
        s.append(el)

# 3. Iterators 
# An iterable is a data type which contains a collection of values which can be processed one by one sequentially. 
# In general, any object that can be iterated over in a for loop can be considered an iterable. 

# While an iterable contains values that can be iterated over, we need another type of object called an iterator to actually retrieve values contained in an iterable. 
# Calling the iter function on an iterable will create an iterator over that iterable. 
# Each iterator keeps track of its position whithin the iterable. 
# Calling next function on an iterator will give the curernt value in the iterable and move the iterator's position to the next value. 


# 4. Generators
# A generator function is a speical kind of Python function that uses a yield statement instead of a return statement to report values. 
# When a generator function is called, it returns a generator object, which is a type of iterator. 

# The yield statement is similar to a return statement. 
# However, while a return statement closes the current frame after the function exits, a yield statement causes the frame to be saved until the next time next is called, which 
# allows the generator to automatically keep track of the iteration state. 

# Once next is called again, exection resumes where it last stopped and continues until the next yeild statement or the end of the function. 
# A generator function can have multiple yeild statements. 

# Including a yield statement in a function automatically tells Python that this function will create a generator. 

# When yield from is called on an iterator, it will yield every value from that iterator. 

def naturals(): 
    current = 1
    while True: 
        yield current 
        current += 1
    

# Questions 4.1
def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) 
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> s = filter(naturals(), is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for elem in iterable: 
        if fn(elem):
            yield elem

def sequence(start, step):
    while True: 
        yield start
        start += step

# Question 4.2
def merge(a, b):
    """
    >>> a = sequence(2, 3)
    >>> b = sequence(3, 2)
    >>> result = merge(a, b)
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    a1, b1 = next(a), next(b)
    while True: 
        if a1 < b1: 
            yield a1
            a1 = next(a)
        elif b1 < a1: 
            yield b1
            b1 = next(b)
        else: 
            yield a1
            a1, b1 = next(a), next(b)
            


