"""
    We want x to be an integer variable and the user to not be allowed to enter any other data type than an integer to be
    stored in x. Hmm... let's see how we can do such...
"""
x = int(input('Enter an integer: '))
"""
    In the above line of code, 
    input("Enter an integer: ") is executed the first => I can enter any type of input I like
    <inputted data is returned by input(...) function>
    int(...) is executed once it gets its input argument => it ensures that the input is an int, otherwise an exception
    is thrown
    <if the argument of int(...) is an integer, that integer is returned, otherwise an exception is thrown>
"""
"""
    Now, I don't want an exception/error to be thrown and "NOT HANDLED", and by not handled I mean that I don't want my
    program to crash if the user enters some input other than an integer
"""
#   tadaaaa :D, TRY-CATCH STATEMENTS
try:
    x = int(input('Enter an integer: '))   # try block of code
except:
    print('That\'s not a valid option!')   # except block of code
    # to print the inverted comma character: print('\'')
"""
    So suppose as a user you forgave this program and decided to enter an integer as you were asked to in line 5, but
    then decided to not enter an integer when line 20 runs. This time, the try block when receives an exception, the 
    except block runs and the program does not crash :P. AHAAA, EXCEPTION HANDLED!
"""
#   But, this is not satisfying unless we ask the user to input the value of x again (until correctly entered)
#   tadaaaa :D, WHILE LOOP
while True:
    try:
        x = int(input('Enter an integer: '))
        break
        # this break statement allows us to break from the infinite loop once the try block is successfully executed
    except:
        print('That\'s not a valid option!')
#   Now let's try inputting a floating number, a complex number etc
while True:
    try:
        y = float(input('Enter a decimal value: '))
        break
        # this break statement allows us to break from the infinite loop once the try block is successfully executed
    except:
        print('That\'s not a valid option!')
while True:
    try:
        z = complex(input('Enter a complex number: '))
        break
        # this break statement allows us to break from the infinite loop once the try block is successfully executed
    except:
        print('That\'s not a valid option!')
