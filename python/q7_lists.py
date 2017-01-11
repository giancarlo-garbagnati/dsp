# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    count = 0

    l = len(words)
    for i in range(l):
        if len(words[i]) > 1:
            if words[i][0] == words[i][-1]:
                count = count + 1

    return count
    #raise NotImplementedError

#print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
#print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
#print(match_ends(['aaa', 'be', 'abc', 'hello']))


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """

    x_list = [x for x in words if x[0] == 'x']
    remainder = [x for x in words if x[0] != 'x']

    return sorted(x_list) + sorted(remainder)

    #raise NotImplementedError


#print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
#print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
#print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    
    # couldn't figure out how to do it with list comprehension, so just went
    #  with a lambda fxn
    sorted_tuples = sorted(tuples, key = lambda x: x[-1])

    return sorted_tuples

    #raise NotImplementedError

#print(sort_last([(1, 3), (3, 2), (2, 1)]))
#print(sort_last([(2, 3), (1, 2), (3, 1)]))
#print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """

    # recursive soln :(
    # if there's a list comprehension / filter+lambda soln I couldn't see it

    def divide_and_compare(nums_list):
        # returns just the list if the length is less than 2
        if len(nums_list) < 2:
            return nums_list

        # if the list has two elements in it, compare and if they are the same, 
        #  delete the last element
        if len(nums_list) == 2:
            if nums_list[0] == nums_list[1]:
                cleaned = nums_list
                cleaned.pop(1)
                return cleaned
            else:
                return nums_list
        
        # divides the list into a list of the last element, and a list of all
        #  the elements before the last
        last = [nums_list[-1]]
        front = nums_list
        front.pop(-1)

        # calls d_a_c on the all the elements but the last
        front = divide_and_compare(front)

        # recombine the two lists
        combined = front + last

        # another check to see if the last and second to last elements are the
        #  same, and removes the last element if so
        if combined[-1] == combined[-2]:
            combined.pop(-1)

        return combined

    '''
    cleaned_nums = [nums[0]] + nums
    cleaned_nums = [ x for x in cleaned_nums[1:] 
                    if cleaned_nums[x] != cleaned_nums[x-1] ]
    return cleaned_nums
    '''
    return divide_and_compare(nums)

    #raise NotImplementedError

#print(remove_adjacent([1, 2, 2, 3]))
#print(remove_adjacent([2, 2, 3, 3, 3]))
#print(remove_adjacent([3, 2, 3, 3, 3]))
#print(remove_adjacent([]))


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    i = 0
    j = 0
    list3 = []

    # two indices to traverse the two lists, adds the lesser element of each
    #  comparison then iterating the list with the lesser element, this
    #  continues until one list runs out
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i = i + 1
        else:
            list3.append(list2[j])
            j = j + 1

    # adds the remainder of whatever list still has elements leftover
    if i == len(list1):
        list3 = list3 + list2[j:]
    else:
        list3 = list3 + list1[i:]

    return list3


    #raise NotImplementedError



#print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
#print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
#print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))
