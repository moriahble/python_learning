print('hi')

# "hi" is called the ARGUMENT of the function--the thing the function acts on. This can also be called a PARAMETER.

print('hello', 'world')

# note that a space is automatically inserted, umlike the plus sign!

#function vs vunction call
# print is the name of a function
# we don't have to call a function; we can just refer to it like we refer to a variable.

other_print = print

other_print('hihi!')

# functions themselves are just another type of value, or OBJECT, and they can be assigned to variables!
# python comes with hundreds of functions; only a handful of which are available automatically

num1 = 5
num2 = 7


def do_math(num1, num2):
    result = num1 * num2
    result = result + 10
    result = result / 1.5
    result = result - num1
    return(result)

print(do_math(num1, num2))
print(do_math(1, 5))
print(do_math(5, 1))
print(do_math(8, 10))

import operator 
print(operator.add(2, 2))
print(operator.not_(True))

# it's generally frowned upon to mix imports in line by line. should be at the top of the code.

# some python functions can have optional arguments; the "equals seven" below is the DEFAULT value of the argument; also called a KEYWORD ARGUMENT

def do_math(num1, num2=7):
    result = num1 * num2
    result = result + 10
    result = result / 1.5
    result = result - num1
    return(result)

print(do_math(5))

def other_function(arg1, arg2 = 'a', arg3 = None, arg4 = True, arg5 = 'hello'):
    pass

other_function(1, arg4 = False)

# python doesn't knkow which keyword argument you're trying to assign