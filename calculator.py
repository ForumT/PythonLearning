def calculator(operator, number1, number2):
    match operator:
     case '+':
       return number1 + number2;
     case '-':
       return number1 - number2;
     case '*':
       return number1 * number2;
     case '/':
       if (number2 == 0):
        return 'Division by 0 is not allowed'
       return number1 / number2;
     case '_':
       return 'Invalid operator'