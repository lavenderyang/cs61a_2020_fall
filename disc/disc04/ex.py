# Disucssion 04
# Tree Recursion
# As a general rule of thumb, whenever you need to try multiple possibilities at the same time, you should consider using tree recursion. 

# Questions
# 1.1. You want to go up a flight of stairs that has n steps. You can either take 1 or 2 steps each time. How many different ways can you go up this flight of stairs? Write a function count_stair_way that solves this problem. Assume n is positive. 
# A: When there is only 1 step, there is only one way to go up the stair. When there are two steps, we can go up in two ways: take a two_steps, or take 2 one-steps. 

# Before we start, what's teh base case for this question? What is the simplest input? 
# A: Our first base case is whereh there are no steps left. This means that we took an action in the previous recursive step that lead to our goal of reaching the top. Our second base case is where we have overstepped. This means that the action we took is not valid, as it caused us to step over our goal. 
def count_stair_ways(n):
    if n == 0 :
        return 1
    elif n < 0: 
        return 0
    else: 
        return count_stair_ways(n-2) + count_stair_ways(n-1)

# 1.2 Tutorial: Consider a special version of the count_stairways problem, where instead of taking 1 or 2 steps, we are able to take up to and indcluding k steps at a time. 
def count_k(n, k): 
    """
    >>> count_k(3, 3) #3, 2 + 1, 1 + 2, 1 + 1 +1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    if n == 0: 
        return 1
    elif n < 0: 
        return 0
    else: 
        i, total = 1, 0
        while i <= k: 
            total += count_k(n-i, k)
            i += 1
        return total

# 2. Lists
# A sequence is an ordered colleciton of values. 
# It has two fundamental properites: length and element selection. 

# List need not be homogenous. 
# Lists can be created using square braces. Their elements can be accessed (or indexed) with square braces. 
# Lists are zero-indexed: to access the first element, we must index at 0; to access the ith element, we must index at i - 1. 
# We can also index with negative numbers. These begin indexing at the end of the list, so the index -1 is equivalent to the index len(list) - 1 and index -2 is the same as len(list) - 2

# List Slicing 
# If we want to access more than one element of a list at a time, we can use a slice. 
# Slicing a sequence is very similar to indexing. 
# We specify a starting index and an ending index, separated by a colon. 
# Python crates a new list with the elements from the starting index up to (but not including) the ending index. 
# We can also specify a step size, which tells Python how to collect values for us. 
# A nagative step size indicates that we are stepping backwards through a list when collecting values. 

# List Comprehensions

# 2.2 Tutorial 
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]

# 2.3 
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive element of s.

    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not s: 
        return 1
    else: 
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))

