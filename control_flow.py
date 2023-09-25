# simplest control flow is a CONDITIONAL
# if the condition is true, the code runs, if not, it can move on

if True:
    print('true')
else:
    print('false')
    

a = 5
# use single = for assignment; double == for checking equivalence

def what_is_a(a):
    if a == 5:
        print('a is 5')
    elif a == 6:
        print('a is 6')
    elif a == 7:
        print('a is 7')
    else:
        print('a is not 5, 6, or 7')

what_is_a(a)
what_is_a(6)
what_is_a(10)

# other useful control statement is a FOR LOOP
for letter in ['a', 'b', 'c', 'd', 'e']:
    print(letter.upper())