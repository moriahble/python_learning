variable_1 = 2
variable_2 = 2
print(variable_1 + variable_2)

print(variable_1 - variable_2)

variable_1 = 4
variable_2 = 5
print(variable_1 * variable_2)

#test comment

str_1 = 'hello'
str_2 = 'world'
print(str_1 + str_2)

print(str_1 + ' ' + str_2 + '!')

a = True
b = False

print('a: ', a)
print('b: ', b)

# "not" reverses the value of a boolean

print('not a: ', not a)
print('not b:', not b)

# "and" looks at both sides; only returns True  if both sides are True

print('a and b: ', a and b)

# "or" looks at any side; returns True if any is True

print ('a or b: ', a or b)

# Booleans, strings, and integers are TYPES
# typeError: cannot use PLUS operator to mix integers and strings
#       print (1 + 'hi')
#           > produces an error
# what does it even mean to add a number to a word? 
# words must be converted to a string for concatenation

print ('1' + 'hi')

# numbers with decimals are called FLOATs - stands for "floating point number"

print(type(12.5))
print(type('a'))
print(type(True))