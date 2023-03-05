from calculator import calculator
# import sys


def output():
  number1 = float(input('Enter 1st no'))
  number2 = float(input('Enter 2nd no'))
  operator = input('Enter the operator')
  answer = calculator(operator, int(number1), int(number2))
  return answer
  # print('the result is ', answer)
