print('What is your name?')
name = input()
if name == 'Tchalla':
    print('Hello, ' + name + ' , my king.')
elif name == 'Malcolm':
    print('Oh, hey there, Malcolm!')
elif not name:
    print('You dare ignore my enquiry?!')
else:
    print('You must be new to these lands.')
print('Very well. What is the password?')

password = input()
if password == 'heartshapedherb':
    print('You may enter')
    print('You have entered the city.')
elif not password:
    print('Is this a game to you?!')
    print('Guards, seperate their head from their body!')
else:
    print('Guards, sieze them!')
    print('You have been expelled from the city.')