
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name = input('Enter a name (blank to quit): ')
    if name == '':
        break

    if name in birthdays:
        print('{} is the birthday of {}'.format(birthdays[name], name))
    else:
        print('I do not have birthday information for {}'.format(name))
        bday = input('What is their birthday?')
        birthdays[name] = bday
        print('Birthday database updated')