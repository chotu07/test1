# list is a collection of homogenous and heterogenous data types
l=[1,2,3,4]
type(l)
list=[1,2,3,4,5]
print(list[0])
#1.append is used to add one more
l=[1,2,3,4]
l.append(5)
print(l)
#2. extend is used to add or merge the two lists
l1=[1,2,3,4]
l2=[5,6,7]
l1.extend(l2)
print(l1)
#3.remove is used to eliminate the value
l=[1,2,3,4]
l.remove(4)
print(l)
#4.insert is used to add the value in a required index position
l=[2,3,4,5]
l.insert(0,1)
print(l)
#5.pop is used to delete the last index value from the list
l=[1,2,3,45,6,7]
l.pop()
print(l)
#6. sort is used to give the priority to integers even strings also presented in the list
l=[3,2,4,1]
l.sort()
print(l)
#7.reverse is used to be as it is
l=[1,2,3,4,5]
l.reverse()
print(l)
#2. tuple

#1.index is used to used to find the index value
t=(1,2,3,4,5)
t.index(4)
print(t.index(4))
l=[1,2,3,4,5]
l.index(2)
print(l.index(2))
#2.count is use dto find the number of accurences
t=(1,2,2,2,3,4,4,5)
t.count(2)
print(t.count(2))
#3.string is collection of words enclosed between quatations
s="python"
s="welcome to python"
# string formating
s1="welcome to"
s2=" python"
print (s1+s2)
age = 22
address = "banglore"
s=" age is %s, and im living in %s"%( age, address)
print(s)
# string methods
#1.upper is used to covert the letters into uppercase
s="welcome"
print(s.upper())
#2.lower
s="PYTHON"
print(s.lower())
#replace
s="wlcome to python"
print(s.replace("python","banglore"))
#strip is by default removes starting space
s=" welcome to python "
print(s)
s="wlcomreto python"
print(s.strip("python"))
#index
s="hello"
print(s[0])
print(s[-1])
# to count no of accurances
s="welcome"
print (s.count("w"))
print(s.count("o"))
#split
s="welcome to python"
print(s.split('o'))
print(s.split('to'))
s="welcome to python"
print(s.startswith("python"))
#capitalise is used to make the first capital letter
s="welcometp python"
print(s.capitalize())
s="welcome to world"
print(s.find('wo'))
#4.format
s="welcome to world"
print(s.format())
#slicing can be used to find the subsequence based on index
l=[1,2,3,4,5,6,7,8,9]
print(l[3:])
print(l[3:7])
print(l[-4:])
print(l[-5:-1])
print(l[0:-1])
s=["welcome to python"]
print(s[:-1])
print(s[-6:])
#control flow statements
#1.conditional statements
#1.simple if
n=10
if n%2==0:
    print('even')
#if else
n=5
if n%2==0:
    print('even')
# else:
#     print('odd')
# n=2
# if n==1:
#     print('english')
# elif n==2:
#     print('hindi')
# elif n==3:
#     print('telugu')
# #programme
# n=2
# if n==2:
#     print('hello')
# else:
#     print('not valid')
#2.looping statements
# #1.for loop
# l=[1,2,3,4,5]
# for i in l:
#     print(i)
# list=[1,2,3,4,5,6,7,8]
# even=[]
# odd=[]
# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#         print(even)
#         print(odd)

#while loop
# n=1
# while n<=10:
#     print(n)
a=1
even=[]
odd=[]
while a<=10:
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
    a+1
print(even)
print(odd)


