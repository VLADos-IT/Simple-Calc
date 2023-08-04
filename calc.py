a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
print('What action you want do with this numbers?')
action = input()

result = None

if action == '+':
    result = a + b
elif action == '-':
    result = a - b
elif action == '*':
    result = a * b
elif action == '/':
    result = a / b
else:
    print('Not supported action!')

if result is not None:
    print('Result:', result)
wait = input("PRESS ENTER TO CONTINUE... ")
