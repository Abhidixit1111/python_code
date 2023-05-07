         #global and local variable        

'''def abc():
    global a
    a=10
    print(a)

abc()


print(a)'''

         #recursion

'''def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result

print("factorial=",fact(5))


         #Factorial

x=int(input("enter number"))
y=1
z=0
for y in range(x+1):
    if y==1:
        z=1
    else:
       z=y*z

print(z)


        #lambda function

x=lambda a,b: a*b
print("mul is=",x(10,10))


        



def abc(**numbers):
   for key, value in numbers.items():
       print("%s==%s" %(key,value))

abc(first="fasf0",imd="sfs",last="agga",zxf="aggag")


     #using map and lambda fun

l=[12,23,34,12,13,14,15,4,15]
def check(x):
    if x>=18:
        return True
    else:
        return False
check=lambda a: True if a>=18 else False
    
y=list(filter(check,l))
print(y)'''



























