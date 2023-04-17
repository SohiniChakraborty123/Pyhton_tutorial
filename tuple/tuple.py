#  tuple is an immutable datastructure so we cannot update delete 
# tuple is ordered datastructure it supports indexing and slicing

t=(10,20,30,45)
print(t,type(t))
#help(tuple)
print(t[0])
print(t[-1])
print(t[:3])

# index and count we have

t=(10,20,20,30,40,50)
print(t.index(20))# gives you the first occurance
print(t.count(20))# gives you the total no of element have in tuple


#enumurate function: allows us to iterate through a sequence but it kepps track of both the index and the element used in tuple string and list.
 
l=[10,20,30,40,50]
for index,value in enumerate(l):
    print(value,index)
 # enumerate function returns a tuple 
for t in enumerate(l):
    print(t)

for t in enumerate(l):
    print(t[0])# it returns the indexes
for t in enumerate(l):
    print(t[1])# it returns the values

# how to convert a list into tuple
l=[20,78,56,90]
t=tuple(l)
print(t)

# if we convert a tuple to the list

t=(20,78,56,90)
l=list(t)
print(l)
