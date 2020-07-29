from pprint import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
    # add character to dict if it doesn't exist
    count.setdefault(character, 0)
    count[character] += 1

print(count)
pprint(count)
