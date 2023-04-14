# how to update and delete element in list
l=[10,20,30,40,50]
l[2]=300
print(l)

#pop
#remove
#clear
#del

l.remove(20)
print(l)

l1=[10,20,30,30,20,40,50]
l1.remove(20)
print(l1)# it only remove ist value which comes first

# if you remove all the element from the list
l1.clear()
print(l1)


# More buildin functions
l=[50,40,30,20,10]
l.sort()# it will not return  if you have print also it will return nothing because it just modify this
print(l)


# reverse the list
l.reverse()
print(l)

l3=sorted(l)
print(l3)# same as sort but it is used in any datatype

print(l.index(30))# find the index l=of the list
print(l.count(30))

l=[10,20,30,40]
l2=[100,200,300]
print(l+l2)

# another example
l=0.5
print(l*4)


