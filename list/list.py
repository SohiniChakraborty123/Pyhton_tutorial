#list
# lists are mutable that means add ,update,delete
# lists are ordered data structure  it supports indexing and slicing 
# lists support heterogenous datatype
l=[10,20,30,40]
print(type(l))

l=[10,20,30,40,"python","java",[100,200,300]]
print(l)

#indexing and slicing
print(l[-1][1])
#print(l[20])# it will give you a error

#slicing
m=[90,78,46,23,"sohini","tom cruise"]
print(m[::-1])

l=[100,200,300,400,500]
for value in l:
    print(value)
for value in l[::2]:
    print(value)

#append
list=[89,90,67,45,67]
list.append(20)
print(list)

#extend is the function where we can add a entire list inside a list
list.extend([200,86,45])
print(list)

#difference between append and extend in :
#append will add a list as a single unit
#extend will add the indiviual element

# if I add a string
list.extend("python")
print(list)# python will iterate as "p","y".... and so on


#insert : add only one  value in the particular position

list.insert(1,1000)
print(list)

l=[10,20,30,45]
l.append(89)
l2=l
print(l,l2)
print(id(l))
print(id(l2))# here memory locations are same and the value will update in both list

# when we use copy funtion it will have different memory location that why if something modify it will show in the first list
l=l2.copy()
l.append(40)
print(l,l2)

