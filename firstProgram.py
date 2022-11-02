# Program to print hell, name and other info
print('What up witcha, playa?')
print('What yo name is?')
myName = input()
print('Okay, ' + myName + '. So, ' + str(len(myName) + 1) + ' is your lucky number. ' + 'And how many rotations have you been here for?')
myAge = int(input())
if myAge > 13:
    print(str(myAge) + ', huh? Thats ' + str(myAge - 13) + ' fewer than me, king.')
else:
    print('You still pretty green then, young blood.')