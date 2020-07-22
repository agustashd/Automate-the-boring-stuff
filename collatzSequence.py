
def collatz(number):
    number = number//2 if number%2 == 0 else (3*number) + 1
    print(number)
    return number

while True:
    try:
        print('Please enter a number: ', end='')
        number = int(input())
        break
    except ValueError:
        print('That\'s not a number')

while number != 1:
    number = collatz(number)

