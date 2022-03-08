# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input("Introduce una palabra:")
userWord = userWord.upper()

for letter in userWord:
    # Complete the body of the for loop.
    if(letter == 'A'or letter == 'E' or letter =='I' or letter =='O' or letter == 'U'):
        continue
    else:
        print(letter)
