
'''
Write a program to find out how often a streak of six heads or tails comes
up in a randomly generated list of heads and tails.
'''

import random

numberOfTests = 10000
numberOfRuns = 100
heads, tails = 0, 0
totalStreaks = 0
streakInRuns = 0
for experimentNumber in range(numberOfTests):
    # Code that creates a list of 100 'heads' or 'tails' values.
    numberOfStreaks = 0
    for test in range(numberOfRuns):
        result = random.randint(0, 1)
        # Code that checks if there is a streak of 6 heads or tails in a row.
        if result == 0:
            heads = heads + 1 if heads < 6 else 1 # if I want to track the event of more than one streak 
            tails = 0
        else:
            tails = tails + 1 if tails < 6 else 1 # if I want to track the event of more than one streak
            heads = 0
        if heads == 6 or tails == 6:
            numberOfStreaks+=1

    totalStreaks+= numberOfStreaks
    streakInRuns = streakInRuns + 1 if numberOfStreaks > 0 else streakInRuns

print(f'The total number of streaks was {totalStreaks}')
print(f'Chance of streak per run: {((streakInRuns / numberOfTests)* 100):.2f}%')