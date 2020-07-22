
'''
Write a function that takes a list value as an argument and returns a string with all
the items separated by a comma and a space, with and inserted before the last item.
For example, passing the previous spam list to the function would return 
'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
 Be sure to test the case where an empty list [] is passed to your function.
spam = ['apples', 'bananas', 'tofu', 'cats']
'''

def concatenate(valueList):
    if valueList == []:
        print('The list is empy')
    elif len(valueList) == 1:
        print(valueList[0])
    else:
        lastOne = valueList.pop(-1)
        print(', '.join([str(val) for val in valueList]) + ' and ' + lastOne)

test1 = ['apples', 'bananas', 'tofu', 'cats']
test2 = []
test3 = [1, 'bananas', 3, 'cats', 'END']
test4 = ['one']
test5 = ['one', 'two']
tests = [test1, test2, test3, test4, test5]

for test in tests:
    concatenate(test)