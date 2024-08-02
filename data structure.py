#data s tructure

'''1,list
2,tuple
3,dictionary
4,set'''

#list (orderd,indexed,duplication allowed,mutable(change))

'''a=["hello",23,"red",22.22,True,"black",33,"red"]
print(a)
print(type(a))'''

# create a list by using list function
'''b=list((1,2,3,4,5))
print(b)'''

#Iteam get from list by index
'''print(a[0])
print(a[3])'''
#19/07/2024

#length
'''print(len(a))'''

# new iteam add imto list
#1 append ()-> added into last position
'''a.append('orange')
print(a)
a.append(1000)
print(a)'''

#insert()-> an iteam add into specified position
'''a.insert(1,'apple')
print(a)'''

#replace an iteam in list
'''a[3]='gray'
print(a)'''

#an iteam delte from list
#1,pop()->lat iteam delete
'''a.pop()
print(a)'''

#2,pop(index)
'''a.pop(4)
print(a)'''
#3,remove -> specified iteam deleted
'''a.remove("black")
print(a)'''

#index()->find index number
#print(a.index('black'))
#count()
'''print(a.count('red'))'''

#number list
'''num=[23,5,1,2,9,5]'''

#sum
'''print(sum(num))'''
#max
'''print(max(num))'''
#mim
'''print(min(num))'''



#sort
'''num.sort()
print(num)'''

#sorted
'''print(sorted(num))'''

#del->delete whole list
'''del a
print(a')'''

# thaye thaye kittaan
'''a=["hello",23,"red",22.22,True,"black",33,"red"]
i=0
max_length=len(a)-1
while i<=max_length:
    print(a[i])
    i+=1'''


#another method in for loop
'''for i in a:
    print(a)'''


# range ( started ,end,step)
'''print(list (range(12)))
print(list (range(3,20)))
print(list (range(4,20,3)))'''

#colors
'''b=['red','black','white']
c=[]
for i in b:
    max=len(i)
    c.append(max)
print(c)'''    

#tuple
'''thistuple=("apple","banana","cherry")
print(thistuple)'''

#tuple length
'''thistuple=("apple","banana","cherry")
print(len(thistuple))'''

# create tuple with one iteam
'''thistuple = ("apple",)
print(type(thistuple))'''
#NOT a tuple
'''thistuple = ("apple")
print(type(thistuple))'''

# tuple data types

'''tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)'''
#type
'''mytuple =("apple","banana","cherry")
print(type(mytuple))'''

#he tuple() Constructor
'''thistuple = tuple(("apple", "banana", "cherry"))'''
# note the double round-brackets
'''print(thistuple)'''

#22/07/24

#Dictionary (key:value) (ordered,unindexed,key unique,mutable)

'''student={'name':'john','age':20,'place':'calicut',23:76,'location':'calicut'}'''
'''print(type(student))
print(student)'''

#1,value access from a dictionary by using key
'''print(student['age'])
print(student['location'])'''
'''print(student['data'])'''#key error,bcz data is not defined

#2.get()

'''print(student.get('place'))
print(student.get(23))'''
'''print(student.get('data'))'''#none will occur
# creating a dictionary by using dict function
'''a=dict([('employee','tom'),('salary',100000)])
print(a)'''
'''B=[('a','b','c'),(3,4),('d','e','f'),{2:33,4:'hell'},[1,2,3]]
print(B)'''
#1,updating a value of key
'''student["age"]=[90,22,33]
print(student)'''

#2,updating a key value pair in dictionary
'''student['color']='red'
print(student)'''

#2,update()
'''student.update({'subject':'english'})
print(student)'''

#clear-> dictionary remains,data deletd
'''student.clear()
print(student)'''

#len
'''print(len(student))'''

#deleting a pair from dictionary

#1,popitem() ->last pair deleted
'''student.popitem()
print(student)'''

#2,pop()
'''student.pop('age')
print(student)'''

#3,del

'''del student['name']
print(student)'''
#del -> deleting dictionary
'''del student'''
#copy
'''sam=student.copy()
print(sam)'''

#any function()-> eetelum 1 true aayal true aaykm
'''mydict={False:'red',False:'black'}
print(any(mydict))

mydict={True:'red',False:'black'}
print(any(mydict))'''

#all function()-> randum true aayal true return cheyym
'''mydict={True:'red',False:'black'}
print(all(mydict))

 mydict={True:'red',True:'black'}
print(any(mydict))'''

#sorted
'''d={1:'red',8:'black',3:'violet',23:'black',5:'gray'}
print(sorted(d))'''

#23/07/2024

#set (collection of unique data)(unordered,unindexed,duplication not allowed)

mixed_set={'hello','red',23,'blue',45,9,12,True,'red'}
'''print(mixed_set)'''

#x=set[] #empty set
'''print(type(mixed_set))'''
#creating a set by using set function

'''a=[1,45,3,7,8,9]
b=set(a)
print(b)'''
#add new item into an set
#1,add()
'''mixed_set.add('apple')
mixed_set.add(90)
mixed_set.add(('html','css'))
print(mixed_set)'''              
#update
'''mixed_set.update('kiwi')
print(mixed_set)

mixed_set.update(('orange','banana'))
print(mixed_set)'''


#delete an item from set

#discard()
'''mixed_set.discard('hello')
print(mixed_set)
mixed_set.discard('hi')
print(mixed_set)'''

# remove()
'''mixed_set.remove('blue')
print(mixed_set)
mixed_set.remove('hi')
print(mixed_set)'''

#clear del len copy
# union |
'''
a={10,20,30,40,50,90,60}
b={20,36,30,77,45,90,11}

print(a|b)'''

# intresection &
'''print(a&b)'''

#difference =>
'''print(a-b)'''
# symmetric difference (a^b)
'''print(a^b)'''

# 29/07/2024

#function(independend block of code wich only runs when its called,code reusability)
'''
1,built-in function->eg,range,print
2,user defined functions
'''

'''

def sample():
    print('hello world')
sample()    


def numbers():
    print(1,2,3,4,5,6,7,8)
numbers()


def sample(name1,name2):
    print('hello',name1)
    print('hy',name2)
sample('tom','jhon')'''

'''def number(num1,num2):
    print (num1+num2)
number(1,2)
number(25,64)

def number(num1,num2):
    print(num1-num2)
number(25,5)


def addition (num1,num2):
    totel=num1+num2
    print(totel)
addition(23,22)'''



# local and global

'''data="hello" # global
def index():
    x=34 # local variable
    global y
    y=100
    print('value of data:',data)
index()
print(data)
print(y)
print(data)  '''  

    

#1 positional arguments

'''def addition (num1,num2):
    totel=num1+num2
    print(totel)
x=int(input('enter your num1:'))
y=int(input('enter your num2:'))
addition(x,y)'''


#2 keyword arguments
'''
def student(name,age,subject):
    print('name of student:',name)
    print('age of student:',age)
    print('intrseted subject:',subject)
student(subject='english',name='jhon',age=20)'''

#3 defualt parameters

'''def multiply (a,b):
    print(a*b)
multiply(20,20)    

def multiply (a=10,b=20):
    print(a*b)
multiply(20,20)    
multiply()'''


#
'''lis=[12,23,45,67,90]
def addlis(a):
    x=0
    for i in a:
          x=i+x
    print(x)
addlis(lis)'''

#
'''list=["hello",'banana',"red",'apple','orange',"black","red"]
def length():
    print(len(list))
length()'''

#4 arbitary positinal

'''def students_name(*name):

    print(name[0])
    print(name[1])
    
students_name('john','ram','tom')'''

#5 arbitary keyboard arguments (**keyword)

'''def employee_details():
    employee_details(name='kavin',salary=100000,position='developer')'''

# return

'''def add(a,b):
    return a+b
print(add(2,3))'''

# function pass into another function

'''def add(x,y):
    return x+y

def twice_add(fun,x,y):
    return fun (fun(x,y),fun(x,y))
             

a=5
b=10
print(twice_add(add,a,b))'''

# recursive function( function that call itself)

'''def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
         
print(factorial(5))'''

# module (set of function)

'''import random

for i in range(5):
    print(random.randint(2,30))

import math
print(math.pi)
print(math.sqrt(100))

from math import *
print(pi)
print(sqrt(200))

from math import pi,sqrt
print(pi)
print(sqrt(200))'''

# random
'''import random
r=random.random()
print(r)

import random
y=[100,200,300,400,500,600]
print(random.choice(y))

# date time
import datetime
x= datetime.datetime.now()
print(x)

# year

import datetime
y= datetime.datetime.now()
print(y.year)

# minute
import datetime
z= datetime.datetime.now()
print(z.minute)

# second
import datetime
a=datetime.datetime.now()
print(a.second)

# math  factorial 
import math
b= math.factorial(10)
print(b)
#math floor
import math
c=math.floor(2.2)
print(c)
#math ceil
import math
d=math.ceil(5.9)
print(d)

#math sqrt
import math
e=math.sqrt(64)
print(e)'''








#30/07/2024


#lambda function

#syntax

#lambda arguments : expression (it take no.of arguments but exicutive single expression)

'''a= lambda x:x+5
print(a(5))

b= lambda a,b: a+b+5
print(b(2,3))


num=lambda x:'even' if x%2==0 else 'odd'
print(num(6))


t=int(input('enter a number:'))
x=int(input('enter a number:'))

num=lambda t,x:t if t>x else x
print(num(t,x)'''

'''x=int(input('enter a number:'))
b = lambda y:x*10 if y>=15 else  y*5  if y<=5 else y

print(b(x))'''


# map (fun,iterable)
'''def fun(x):
    return x 
num=[1,2,3,4]
a=map (fun,num)
print(list(a))


def fun_rece(x):
    return 1/x
num=[4,8,3]
a=map (fun_rece,num)
print(list(a))'''

'''a= lambda x:1/x
d=map(a,[4,8,3])
print(list(d))'''

'''a=map(lambda x:1/x,[4,8,3])
print(list(a))'''

# filter (function,iterable)
'''def even(z):
    if z%2==0:
        return True
    else:
        return False
num_list=[2,34,5,6,7,8,9,10,65]
data =filter (even,num_list)
print(list(data))'''

# 1/08/2024

# list comphrehensions
# syntax
#new_list=[expression for iteam in iterable if condition==true]

'''fruits = ['apple','banana','kiwi','mango','berry']
          
new_list =[]
for i in fruits:
    if 'a'in i:
          new_list.append(i)
print(new_list)'''


'''new_list=[i for i in fruits if 'banana' not in i]
print(new_list)

numbers= [3,4,8,5]
squares= [i**3 for i in numbers]
print(squares)'''

'''a='codeme'
vowels='aeiouAEIOU'
b=[i for i in a if i in vowels]
print(b)
             
even_num=[i for i in range(1,10) if i%2==0]
print(even_num)'''

'''x=[i*5 for i in range(1,11)if i%2==0]
print(x)'''

# list slicing [start:end:step]
'''a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(a[:])
print(a[3:])
print(a[:7])
print(a[4:10])
print(a[3:12:2])
print(a[::2])
print(a[3::2])
print(a[:14:3])'''

# reverse / negetive slicing 

'''a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
print(a[::-1])
print(a[-2:])
print(a[:-3])
print(a[-5:-2])
print(a[3:1:-1])
print(a[2:-2])
print(a[5:2:-1])
print(a[-1:-4:-1])
print(a[-4:-1:2])
print(a[-2:-5:-1])
print(a[-1:-6:-1])
print(a[-6:-2:-1])
print(a[4:2])'''

# string slicing

'''x=('hello , world')
print(x[0:1])
print(x[1:5])
print(x[-7:-5])
print(x[3:1:-1])
print(x[2:-2])
print(x[5:2:-1])
print(x[-1:-4:-1])
print(x[-4:-1:2])
print(x[-2:-5:-1])
print(x[-1:-6:-1])
print(x[-6:-2:-1])
print(x[4:2])'''

#02/08/2024

#expctional 


'''print('hello')
print(5/0)
print('hi')
    
try:
    print('hello')
    print(5/0)
except ZeroDivisionError:
    print('division by zero')
finally:
    print('hi')'''

'''try:
    a=('hello')
    b=2
    print(a+b)
except TypeError:
    print(' can only concatenate str (not "int") to str')
finally:
    print('python')

try:
    a=['hello','red','kiwi']
    print(a[1])
    print(a[3])
    print(a[0])
except IndexError:
    print('list index out of range')
finally:
    print('python')'''



'''def fun (a):
     if a<4:
         b=a/(a-3)
         print('value of b:',b)
     else:
         print('hello')

try:
    fun(3)
except ZeroDivisionError:
    print('division by zero')
finally:
    print(fun(5))'''


#raise

'''x=-1
if x<0:
    raise Exception('sorry,no numbers below zero')'''


'''print('hello')
raise TypeError('hello')
print('hi')'''










        
    


