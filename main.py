def formula_to_ascii(filename):
    key = {'sp': ' ', 'bS': '\\', 'sQ': "\'"}

    with open(filename, 'r') as file:
        f = file.read()
    chunk = f.split(' ')
    line = ''

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


def ascii_to_formula(filename):
    # Read the content of the file
    with open(filename, 'r') as file:
        art = file.read()

    # Abbreviations
    abbreviations = {
        ' ': 'sp',
        '\\': 'bS',
        '\'': 'sQ',
    }

    # Helper function to add current sequence to the result list
    def add_to_result(mult, character):
        if character.isdigit():
            result.append(str(mult) + character)
        elif character in abbreviations:
            result.append(str(mult) + abbreviations[character])
        else:
            result.append(str(mult) + character)

    # Initialization
    result = []
    current_char = None
    count = 0

    # Iterate through every character in art
    for char in art:
        # Handle newline
        if char == '\n':
            if current_char:
                add_to_result(count, current_char)
                count = 0
                current_char = None
            result.append('nl')
        # Handle same character sequence
        elif char == current_char:
            count += 1
        # Handle change of character
        else:
            if current_char:
                add_to_result(count, current_char)
            current_char = char
            count = 1

    # Handle the last sequence
    if current_char:
        add_to_result(count, current_char)

    return ' '.join(result)


# print(ascii_to_formula('charizard.txt'))
# print(formula_to_ascii('charizardFormula.txt'))
