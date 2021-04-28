'''Task 1
The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.'''

import random
print('I propose to play with me. What is your name?')
name = input()
print('Nice to see you ' + name + '!' + ' Try to guess number from 1 to 10')
number = random.randint(1, 10)
user_number = int(input('Enter the number'))
count = 0
max_count = 5
while number != user_number:
    count += 1
    if count > max_count:
        print(f'Sorry + {name} but you lost! The game is over. My number was' + {number})
        break
    if user_number > number:
        print(f'Attempt N + {count}')
        user_number = int(input('Enter the number'))
        print('my number is less than yours')
    elif user_number < number:
        print('My number is greater than yours')
else:
    print('Great job' + name + '! You won' + count + 'try')

'''Task 2
The birthday greeting program.
Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”   '''

user_name = input('What is your name?: ')
print('Hello ' + str(user_name) + '!')
user_age = input('Provide your age: ')
print(f'{user_name} on your next birthday you’ll be {user_age+1}')

'''Task 3
Words combination
Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)'''

from random import sample
print('Enter a word consisting of 5 letters. For instance, hello.')
word = input()
letters = list(word)
print(''.join(sample(letters,5)))

'''Task 4
The math quiz program
Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.'''

from random import randint
from time import time

print('Try to play a math qiuz')

while True:
    num1 = randint(2, 9)
    num2 = randint(2, 20)
    numbers = num1 * num2
    start_time = time()
    response = input(f'What is {num1} * {num2}? ')
    answer = int(response)
if answer == numbers:
        elapsed = time() - start_time
        print(f'Right, in {elapsed:.2f} seconds')
else: print(f'Wrong, the correct answer was {numbers}')
