'''l=[1,2,3,4,5,6,7]
print(l[0:6])
l1=['a','b',23,'abhishek']
print(l1)

       #creating list using string and tuple

string='abhishek'
tuple=(2,3,4,5,6,7)
list1=list(string)
list2=list(tuple)
print(list1)
print(list2)

print(len(list1))   #getting length of list
print(len(list2))

print(list1[0])      #access element using index
print(list2[0:8-1])  #max=len-1

      #access using slicing

print(list2[0:7:1])
print(list1[0:7:1])

print(list1[0:1])

      #deleting element from list


del list1[0]
print(list1)   #deleting an element from list


print(list1)
del list1[0:3]
print(list1)

s='abhishek'
l=list(s)
print(l)
del l[0:3]  #o/p=['a', 'b', 'h', 'i', 's', 'h', 'e', 'k']
            #    ['i', 's', 'h', 'e', 'k']
print(l)


    #max, min, sorted and sum
l=[5,3,4,8,6,7,2,1]
print(max(l))
print(min(l))
print(sorted(l))
print(sorted(l,reverse=True)) #reverse sort
print(sum(l))    #we can use l.reverse()


  # any and all function




  #append, insert and extend

l=[1,2,3,4,5]
print(l)
l.append(6)
print(l)
l.insert(6,7)
print(l)
l2=[8,9,10]
l.extend(l2)
print(l)

   # remove, pop and del

l=[1,2,3,4,5,6,7,8,9,10]
l.remove(1)
print(l)
l.pop(5)  #pop using index
print(l)
del l[0:3]
print(l)

    #difference b/w sort() and sorted()
   

l=[1,4,36,7,346,67,45,6]
l2=[24,345,345,6,23,424,34]
print(l)
l.sort()
print(l)
print(l2)
print(sorted(l2))'''

    #list comprehension

l=[1,2,3,4,5,6,7,8]
l2=[x*2 for x in l]
print(l2)








