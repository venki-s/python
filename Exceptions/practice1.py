try:
    for i in ['a','b','c']:
        print(i**2)

except TypeError:
    print('Caught Error1')

finally:
    print("finally block1")


try:
    x = 5
    y = 0

    z = x/y

except TypeError:
    print('Caught Error2')

finally:
    print("finally block2")


def ask():

    try:
        int_input = input('Enter Input')
        print (int_input ** 2)
    
    except:
        print('An error occurred please try again')

ask()