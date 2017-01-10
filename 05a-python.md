# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both are sequences of values/elements, but lists are mutable while tuples aren't. Lists are instantiated with square brackets ( "[ ]" ), while tuples are a comma-seperated list of values (sometimes enclosed in parentheses, though not necessary). Lists of tuples can be used to initialize new dictionaries, with each tuple being a key-value pair in the dictionary.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are also a collection of elements, but sets are unordered and contain no duplicates. Sets are instantiated with curly braces ( "{ }" ). Finding a particular element in a set is significantly faster than in lists because sets are implimented as hashtables (similar to a dictionary).

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> ‘lambda’ is an anonymous fxn that is created at runtime. It doesn’t include a return statement, but an expression that which is returned. You can use a lambda definition anywhere a fxn is expected (such as in the parameters of sorted() key parameter, or in filter(), map(), reduce(), etc). Example:

```python
# should returned a resorted list of list a, but with first the odd numbers sorted, then the even numbers sorted
a = [1, 2, 3, 4, 5]
sorted(a, key = lambda f: f%2==0)
# [1, 3, 5, 2, 4]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are another way in python to implement notation for sets used in mathematics. They can be used as a substitute for lambda functions, as well as other functions like map() and filter(). They are similar to the apply() fxns (such as apply(), lapply(), sapply()) in R. Capability-wise and performance-wise they are very similar especially when using a lambda function with map() or filter().

>> map() equivalent example:
```python
## Fahrenheit to celsius
# map() + lambda fxn
f = [32, 57, 98, 212]
c = list(map(lambda x: (x-32)*(5/9), f))
# [0.0, 13.88888888888889, 36.66666666666667, 100.0]
# list comprehension - map
f = [32, 57, 98, 212]
c = [ ((x-32)*(5/9)) for x in f ]
# [0.0, 13.88888888888889, 36.66666666666667, 100.0]
```

>> filter equivalent example:
```python
## Filtering out even numbers
# filter() + lambda fxn
a = list(range(1,11))
b = list(filter(lambda x: x%2==1, a))
#[ 1, 3, 5, 7, 9]
# list comprehension - filter
a = list(range(1,11))
b = [ x for x in a if x%2==1 ]
# [1, 3, 5, 7, 9]
```

>> set comprehension example:
```python
a = set(range(5))
# {0, 1, 2, 3, 4}
# squaring all numbers in this set
b = {x**2 for x in a}
# {0, 1, 4, 9, 16}
```

>> dictionary comprehension example:
```python
# create a dictionary from a string of lowercase letters where the key value is the uppercase character and maps to its lowercase chars
a = "abcdefghijklmnopqrstuvwxyz"
d = {x.upper(): x for x in a}
# 'C': 'c', 'S': 's', 'D': 'd', 'G': 'g', 'X': 'x', 'H': 'h', 'Z': 'z', 'T': 't', 'R': 'r', 'Y': 'y', 'O': 'o', 'A': 'a', 'P': 'p', 'I': 'i', 'K': 'k', 'B': 'b', 'U': 'u', 'W': 'w', 'F': 'f', 'E': 'e', 'V': 'v', 'Q': 'q', 'N': 'n', 'J': 'j', 'L': 'l', 'M': 'm'}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





