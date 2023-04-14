# variables are the containers for storing the value.
# variable is created when we assign a value

#example
x=7
y=90
print(x,y)

a=89
a="sohini"
print(a)# variable has no particular type it changes after been set

# type cast: if you want to specify the datatype you need casting


x=str(3)
u=float(3)
n=int(3)
print(x,u,n)

# rules of declaring variable

# A variable name starts with  a letter or underscore
# Cannot start with number
# only contain (A-z,0-9,and__)
#case sensative
# may not start with keywords


# Camel case: each work except starts with a captital letter
myVariableName="john"
print(myVariableName)


# pascal case: each starts with capital letter
MyVariableName="sohini"
print(MyVariableName)

# SNAKE case: seperated as underscore

My_variable_name="tom"
print(My_variable_name)

# Global varible:
# These are declared outside the function and accesible throughout the code
def f():
    print("inside function")
s="I love eating"
f()
print("outside the function",s)

# local variable: variable are declared inside the function and scope is also inside the function.we cannot access it from outside.


def p():
    s="I love eating"
    print(s)
p()

