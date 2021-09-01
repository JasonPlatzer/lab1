import re

def banner():
    ''' Dispaly program name'''
    message = 'Awesome camelcase program'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}')

def instructions():
    print('Enter a sentence and program will convert it to camelcase.')

banner()
instructions()

to_check = True
while  to_check:
    sentence = str(input("Enter a sentence use only letters "))

    # from automate the boring stuff book
    # and from # from https://www.guru99.com/python-regular-expressions-complete-tutorial.html
    check = re.match(r'[\d\W]', sentence)
    
    if not check:
        

    

        sentence = sentence.lower()
        listWords = []
        split = sentence.split(' ')
        for word in split:
            length = len(word)
            x = word[0].upper()
            listWords.append(x + word[1:length])
        to_check = False
    # from https://www.geeksforgeeks.org/python-string-join-method/
print("".join(listWords))