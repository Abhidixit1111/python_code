

'''x=lambda a:a%2==0
l=[int(a) for a in input("enter elements =").split()]
y=list(filter(x,l))
print(y)

def check(x):
    if x%2==0:
        return x
l=[int(a) for a in input("enter elements").split()]

y=list(map(check,l))
print(y)
z=list(filter(check,l))
print(z)


from functools import *
x=[1,2,3,4,5]
e=reduce(lambda a,b:a+b,x)
#e=sum(x)
print(e)

l=[1,2,3,4,5,6,0,0,False,7]
k=all(l)
print(k)
print(any(l))


     #fun aliasing

def abc(x):
    print("good morning",x)
xyz=abc
xyz("visics")
abc("kanpur")
del abc
#abc("lucknow")
xyz("abhishek")

import math
print(math.pow(2,4))'''

import module1#create a module1 file then define fnction and call
print(module1.average(5,25))






















   
