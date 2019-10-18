Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#set is used to represent the group of values in a single entity
>>> s={10,20,30,40,50}
>>> print(s)
{40, 10, 50, 20, 30}
>>> type(s)
<class 'set'>
>>> 
>>> l={10,20,30,10,30,40,10}
>>> s=set(l)
>>> print(s)
{40, 10, 20, 30}
>>> 
>>> s=set(range(5))
>>> print(s)
{0, 1, 2, 3, 4}
>>> 
>>> s={}
>>> print(s)
{}
>>> type(s)
<class 'dict'>
>>> 
>>> 1.add
SyntaxError: invalid syntax
>>> 
>>> 
>>> #1.add is used to add one more
>>> s={10,20,30}
>>> s.add(40}
SyntaxError: invalid syntax
>>> 
>>> s={10,20,30}
>>> s.add(40)
>>> print(s)
{40, 10, 20, 30}
>>> #2.update is used to add multiple set
>>> s={10,20,30}
>>> l=[40,50,60]
>>> s.update(l,range(5))
>>> print(s)
{0, 1, 2, 3, 4, 40, 10, 50, 20, 60, 30}
>>> #3.copy
>>> s{10,20,30}
SyntaxError: invalid syntax
>>> s={10,20,30}
>>> s1=s.copy()
>>> print(s1)
{10, 20, 30}
>>> #4.pop  is uswed to delete the number from set
>>> s={20,30,40,10}
>>> print(s)
{40, 10, 20, 30}
>>> print(s.pop())
40
>>> 
>>> #5 remove is used to eliminate particular number from set
>>> s={10,20,30,40}
>>> s.remove(30)
>>> print(s)
{40, 10, 20}
>>> 
