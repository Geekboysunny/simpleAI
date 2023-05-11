
import random 


reply = ['Hi, How are you?', 'Thank you for contacting me', 'How may I be of Help to you?']
greeting = ['Hello', 'Hi', 'Salute', 'Hey There', 'Hey']

def greetings(data):

    data = input('Enter word: ')
    if data:
        word = data.capitalize()
    for i in greeting:
        if i == word:
            answer = random.choice(reply)
            print(answer) 

greetings('greeting')


