# Python random module is an build in modules that generate random numbers.this is used for generating numbers, use random values for ay string and list
import random
list=[1,8,9,45,89]
print(random.choice(list))# print random value from the list
# every time you run this code the output will  be change as all the numbers are random value

import random
random.seed(5)
print(random.random())# print seeding value of a random module

#random.randint() generating random integer of a given range

import random
r1=random.randint(5,15)
print("Random number between 5 and 15",(r1))

# Selecting random elements:
#random.choice() is used to return a random item from a list,tuple,string

import random
list1=[1,2,3,4,5]
print(random.choice(list1))
string="sohini"
print(random.choice(string))
tuple=(1,2,4,6,8)
print(random.choice(tuple))

# shuffle list
#random.shuffle(): is used to shuffle a sequence. Shuffling means changing the position

import random
my_list=[12,45,78,54,98]
print("orginal list",my_list)
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)








