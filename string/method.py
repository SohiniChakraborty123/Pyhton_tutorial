#help(str)
#print(dir(str))
# format method
num1=12
num2= 13
#print("value of num1 is {} value of num2 {}".format(num1,num2))# {} is a empty place holder where we can write the value 
#print("value of null is {0} value of num2 {1 }".format(num1,num2))

s ="python sample string"
print(id(s))
s1=s.capitalize()
print(s1)

# upper
# lower
# tittle
print(s.upper())
print(s.lower())
print(s.title())
# check if it is on upper case or not
print(s.isupper())
print(s.islower())
print(s.istitle())
 #isupper()
 #islower()
 #istittle()
  
# split
# join

s="html,css,python, djnago, java"
l=s.split(",")
print(l)

s1=" ".join(l)
print(s1)

s1="abcd"
s2="1234"
s3=" python sample string abcd"
table = str.maketrans(s1,s2)
result =s3.translate(table)
print(result)

#index
#find
#rfind

s="html,Css,Python"
print("Python"in s)
print(s.index("Python"))

 # if i have multiple occurances 
s="html,css,Python,Python,Python"
print("Python" in s)
print(s.index("Python"))
# it will always give the first index how many occurances it will have


print(s.find("Python"))
print(s.find("python"))

# difference between find and index is that when we cannot find the particular string index will return error but find will return -1

print(s.rfind("Python"))# gives the last occurance

# remove white spaces 
s="    This is sample string  "
s1=s.strip(" ")
print(s1)

s="******* Sohini is working********"
s1=s.strip("*")
print(s1)

a="$$$$$corporate's have no life$$$$$$  "
a1=a.lstrip("$")
print(a1)

r="&&&&& This is life &&&&&"
r1=r.rstrip("&")
print(r1)

b= "python"
b1=b.center(20,"*")
print(b1)

m="html,css, python, html"
m1=m.replace("html","html5")
print(m1)# replace the old string to new string
