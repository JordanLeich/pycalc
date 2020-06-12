# Code edited by Jordan Leich on 6/11/2020, email me at jordanleich@gmail.com if you wish to code together!


def calculator():

    # noinspection PyBroadException
    try:
        first_number = int(input("Enter first number: "))
        print()

        operator = input(str("Enter an operation (+ | - | * | /): "))
        print()

        second_number = int(input("Enter second number: "))
        print()

        if operator == '+':
            print(first_number + second_number)

        elif operator == '-':
            print(first_number - second_number)

        elif operator == '*':
            print(first_number * int(second_number))

        elif operator == '/':
            print(first_number / second_number)

        else:
            print('Unknown Operator! Restarting Calculator...')
            print()
            calculator()

    except:
        print()
        print("Error Caught! Restarting Calculator...")
        print()
        calculator()


calculator()
