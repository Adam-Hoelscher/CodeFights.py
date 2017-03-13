def numberSystem(digits, n):

    from math import log

    base = len(digits)
    power = int(log(n)/log(base))

    human_digits = []

    if 0 in digits:
        n -= 1

    while power >= 0:
        current_digit = int(n/(base**power))
        human_digits.append(current_digit)
        n -= (current_digit * base**power)
        power -= 1

    if 0 not in digits and 0 in human_digits:
        non0_digits = [human_digits[0]-1]
        non0_digits += [base - 1 + d for d in human_digits[1:]]
        non0_digits[-1] += 1

        non0_digits = non0_digits[::-1]
        carry = 0
        for i, d in enumerate(non0_digits):
            d += carry
            carry = int((d-1)/base)
            non0_digits[i] = d - carry * base
        non0_digits = non0_digits[::-1]

        alien_digits = [str(digits[d-1]) for d in non0_digits if d != 0]
    elif 0 not in digits:
        alien_digits = [str(digits[d-1]) for d in human_digits]
    else:
        alien_digits = [str(digits[d]) for d in human_digits]

    return(''.join(alien_digits))

if __name__=='__main__':
    digits = [4, 7, 8]
    n = 3274653
    print(numberSystem(digits, n))