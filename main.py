import sys
import math

# Set the file path for the recipe #
path = ''

f = open(path, 'r')
t = f.read()

f.close()

line = ''

key = {'sp':' ', 'bS':'\\', 'sQ':"\'"}

list = t.split(" ")

for x in list:
    numeral = ''
    chars = ''
    if x == 'nl':
        line += '\n'
    elif x.isdigit():
        numeral = x[:-1]
        chars = x[-1]
        line += (int(numeral) * chars)
    else:
        for c in x:
            if c.isdecimal():
                numeral += c
            else:
                chars += c
        if chars in key:
            line += (key[chars] * int(numeral))
        else:
            line += (chars * int(numeral))
    
print(line)
