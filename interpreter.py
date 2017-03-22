def interpreter(program):

    cells = [0]
    position = 0
    i = 0
    output = ''

    while i < len(program):
        token = program[i]
        if token == '+':
            cells[position] = (cells[position] + 1) % 256
        elif token == '-':
            cells[position] = (cells[position] - 1) % 256
        elif token == '<':
            position -= 1
        elif token == '>':
            position += 1
            try:
                cells[position]
            except:
                cells.append(0)
        elif token == '[':
            open = int(cells[position] == 0)
            while open:
                i += 1
                if program[i] == '[':
                    open += 1
                elif program[i] == ']':
                    open -= 1
        elif token == ']':
            open = int(cells[position] != 0)
            while open:
                i -= 1
                if program[i] == ']':
                    open += 1
                elif program[i] == '[':
                    open -= 1
        elif token == '.':
            output += chr(cells[position])

        i += 1

    return output

if __name__=='__main__':
    print(1, 'Cf', interpreter('++++++++++++++[>+++++>-----------<<-]>---.>.'))
