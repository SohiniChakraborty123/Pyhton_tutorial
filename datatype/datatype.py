# datatype
#int
num1=100
print(type(num1))

# float : store decimal numbers

num=89.09
print(type(num))

# interger and float are immutable datatype. We may not change the value after being set

a=100
print(id(a))
a=105
print(id(a))
# memory locations are same

# string: anything within '',"","""
s="python"
print(id(s))
s="sohini"
print(id(s))# immutable

# list:add multiple values enclosed within square bracket
l=[67,89,45,34]
print(l)

# lists are heterogenius we can have different datatype in the list

list=[10,20,30,40,"python","django","flask"]
print(id(list))
list.append(50)
print(id(list))
# it allow me to change because it is mutable

# tuple:
t=(10,20,30,60)
print(t)

# dict:
d={"name":"ABC","email":"abc@gmail.com"}
print(d)

# set{}:mutable  datatype it is allowed to update delete

s={19,20,59,67}
print(s)

# boolean :true false

# complex:4+3j




