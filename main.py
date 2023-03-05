from output import output

while True:
  answer = output()
  if (isinstance(answer, str)):
    print(answer)
  else:
    print('The result is ', answer)
  choice = input('Do you wish to continue? (y/n):')
  if (choice.lower() != 'y'):
    break
