import random

flag = open('flag.txt', 'r').read()
ct = ''

# random.randrange() returns a randomly selected element from the specified range
k = random.randrange(0,0xFFFD)

for c in flag:
    # chr() returns a character from an integer - unicode
    # ord() returns the unicode code from a given character
    ct += chr((ord(c) + k) % 0xFFFD)


open('out', 'w').write(ct)

# Note that if (ord(c) + k) is less than 0xFFFD, then
# (ord(c) + k) % 0xFFFD will be equal to (ord(c) + k)

# The symbols in unicode get out of bounds for the typical flag around decimal value 128, 0x0080.

# 0xFFFD = 65533 in decimal
# (65533 - 128)/65533 = a 99.8% chance that the random number picked for var k will not add enough to the flag characters that the modulus will alter the resulting character.

# We should be able to just brute force the flags:
    # Take the characters from the out file
    # start by subtracting one from the unicode value of each character and then converting it back to a unicode character
    # print the result to a file
    # each iteration from 1 to 65405 (65533 - 128) subtract the iteration number and repeat these steps
    # grep the output file for a string that starts with 'flag{'

# if there is no flag present in the output file then the random number used to encrypt must be between 65405 and 65533


