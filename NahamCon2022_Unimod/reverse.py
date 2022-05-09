ct = open('out', 'r').read()

# possible flag, temp buffer while iterating, cleared at the end of each iteration if flag is not found.
pf = ''

# need to get lowest value unicode character from the out file, because we can't subtract an equal or greater amount from any given character.
lowestunival = 65405
for c in ct:
    if ord(c) < lowestunival:
        lowestunival = ord(c)

# Working our way back from the higher value because I believe the plain text characters will be between 0 and 127 in value.
for i in range(lowestunival, 1, -1):
    for c in ct:
        # chr() returns a character from an integer - unicode
        # ord() returns the unicode int value from a given character
        pf += chr((ord(c) - i))

    if(len(pf.split('flag{')) > 1):
        print(pf)
        print('Flag found for shift value of {}'.format(i))
        exit()
    pf = ''
