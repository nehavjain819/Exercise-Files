# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)


# re-declaring the variable works
f="neha"
print(f)


# ERROR: variables of different types cannot be combined
# print("neha " + 123)
# Global vs. local variables in functions
def fun():
    f="somevalue"
    print(f)

fun()
print(f)

