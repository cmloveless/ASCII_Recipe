
key = {'sp': ' ', 'bS': '\\', 'sQ': "\'"}


def formula_to_ascii(formula):

    line = ''
    chunk = formula.split(" ")

    for x in chunk:
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
    return line
