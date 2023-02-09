def isPalindrome(word):
    word = word.replace(" ", "")
    word = word.replace("á", "a")
    word = word.replace("é", "e")
    word = word.replace("í", "i")
    word = word.replace("ó", "o")
    word = word.replace("ú", "u")

    a = 0
    b = len(word)-1

    for i in range(0, len(word)):
        if word[a] == word[b]:
            a+=1
            b+=1
        else:
            return False
    return True


word = input('Enter a word or sentence here: ').lower()

if isPalindrome(word):
    print('The word or sentence is palindrome')
else: 
    print('Not is a word or sentence palindrome')