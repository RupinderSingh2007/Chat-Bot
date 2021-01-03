import random

helloo = ["hi","is anyone there?","hello", "good day","hello there"]
bye = ["bye","see you later","goodbye","i am leaving","have a nice day"]
howareyou = ["how are you","how are you?","whats up?","how you doing"]
name = ["whats your name?","what is your name?","do you have any name?"]
subscribe = ["who is my technology store?","Bye"]

print("---------------------------------------------------------------------------------\n")

while True:
    a = input('User Said - ')

    if a.lower() in helloo:
        botans = ["Hello","hi","hola","hi there","hello!"]
        print('Bot Said - '+random.choice(botans)+'\n')

    elif a.lower() in bye:
        botans = ["Okay , Bye","Thankyou for coming"]
        print('Bot Said - '+random.choice(botans)+'\n')

    elif a.lower() in howareyou:
        botans = ["I am Fine What about You?"," I am Good","I am Okay!"]
        print('Bot Said - '+random.choice(botans)+'\n')

    elif a.lower() in name:
        botans = ["My name is Jarvis 2.0","You can Call Me Jarvis 2.0","My Friends call me Jarvis 2.0"]
        print('bot Said - '+random.choice(botans)+'\n')

    elif a.lower() in subscribe:
        botans = ["My Technology Store is a channel who creates videos of technology please subscribe to it"]
        print('Bot Said - '+random.choice(botans)+'\n')

    else:
        print('Bot Said - Sorry What ?''\n')
