# string will be '',"",""" is a valid string
# String are immutable once I define a string I can't modify a value  with same memory location
# string is ordered data structure it will support indexing and slicing


s2="pyhton"
print(id(s2))
s2="java"
print(id(s2)) 


s="Python sample string"# it will start 0 from left  side

print(s[0])
print(s[1])
print(s[2])
print(s[-1])# it will start from right as -1


# slicing
print(s[0:6])# [start:end] 0 to n-1
print(s[7:])
print(s[:6])
 # stride
print(s[::3])# is starts from 0 like p but skip 3  letters 
print(s[::-1])# it will reverse the string from right side

print(s[::-2])# it will reverse the string but every second index

# suppose you have given wrong indexing as per indexing it will return indexing error but slicing will show null value  
print(s[6:0])

# loop in string
for value in s:
    #print(value)
    print(s[2:])

