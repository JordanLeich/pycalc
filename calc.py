# This is a code for addition and subtraction
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    num0, num1 = float(num0), float(num1)
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1n
    else:
        print('unknown operator!')
        return None
