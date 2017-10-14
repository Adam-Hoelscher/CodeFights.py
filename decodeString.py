from string import ascii_lowercase as letters
digits = '1234567890'

def decodeString(s):

    stack = []
    string = [x for x in s]

    def calc(chars, mult = 1):
        if stack:
            temp = stack.pop()
        else:
            temp = ''
        if temp == ']': temp = ''
        stack.append(mult * chars + temp)

    while string:
        if string[-1] == '[':
            string.pop()
            continue
        if string[-1] == ']':
            stack.append(string.pop())
            continue
        if string[-1] in letters:
            calc(string.pop())
            continue
        if string[-1] in digits:
            mult = string.pop()
            if string:
                while string[-1] in digits:
                    mult = string.pop() + mult
                    if not string: break
            calc(stack.pop(), int(mult))
            continue

    return(''.join(stack))
