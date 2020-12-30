#
# Example file for working with functions
#

# define a basic function
def fun():
    print("I am a function")

# function that takes arguments
def fun2(arg1,arg2):
    print(arg1, " " , arg2)

# function that returns a value
def cube(x):
    result = x*x*x
    return result

# function with default value for an argument
def power(num,p=1):
    result = 1
    for i in range(p):
        result = result * num
    return result

#function with variable number of arguments
def mul_add(*arg):
    result = 0
    for i in arg:
        result = result + i
    return result
# fun()
# print(fun())
# print(fun)

print(cube(4))
print(power(2))
print(power(2,3))
print(power(p=3,num=4))
print(mul_add(2,3,4,5))