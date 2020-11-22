def streamValidation(stream):

    if not stream:
        return True

    head = f"{stream[0]:08b}"
    blocks = head.find('0')

    if blocks == -1:
        return False
    elif blocks == 0:
        return streamValidation(stream[1:])
    elif blocks > len(stream):
        return False
    else:
        tail = stream[1:blocks]
        if not tail:
            return False
        for block in tail:
            if f"{block:08b}"[:2] != '10':
                return False
        return streamValidation(stream[blocks:])
