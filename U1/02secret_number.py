import random
secret_number= random.randrange(100)
print('The secret number is between 1-100')
num = int(input('Guess the secret number: '))
numero_intentos=0

while num != secret_number:
    numero_intentos+=1
    if num < secret_number: 
        num = (int(input('Enter a higher number: ')))
    elif num > secret_number:
        num = (int(input('Enter a lower number: ')))
print('Bingoo:D')
print('Your number of attempts was: ', numero_intentos)