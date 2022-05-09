def readFile():
    ct = open('out', 'r').read()
    ctArr = []

    for x in ct:
        ctArr.append(ord(x))
    return ctArr

sortedArr = readFile()
sortedArr.sort()

print('Highest Value: {}\nLowest Value: {}\nRange: {}'.format(sortedArr[-1], sortedArr[0], (int(sortedArr[-1]) - int(sortedArr[0]))))


unsortedArr = readFile()

print("\nOut File Encrypted Characters:\n", unsortedArr)

pt = []

for x in unsortedArr:
    pt.append(chr(x-39137))

print('\nOut File Characters after shifting left by 39137\n', pt)

flag = ''.join(pt)

print('\nFlag:\n', flag)


