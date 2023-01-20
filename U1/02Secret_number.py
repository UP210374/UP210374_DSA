import random
secret_number= 9

print('\nWelcome to the guess the guesser game', '\n')
print('The secret number is between 1-1000\n')
num = int(input('Guess the secret number: '))
numero_intentos=1

while num != secret_number:
    numero_intentos+=1
    if num < secret_number: 
        num = (int(input('Enter a higher number: ')))
    elif num > secret_number:
        num = (int(input('Enter a lower number: ')))
print('Bingoo:D \nThe secret number was: ', num)
print('Your number of attempts was: ', numero_intentos)