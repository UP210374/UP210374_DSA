from random import randint

def fillArray(n):
    array = []

    for row in range(n):
        row2 = []

        for col in range(n):
            row2.append(randint(1,1000))

        array.append(row2)
    
    return array

result = fillArray(5)

print(result)