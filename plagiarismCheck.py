import re


def plagiarismCheck(code1, code2):

    code1 = '\n'.join(code1)
    code2 = '\n'.join(code2)

    def regex_iter(code):
        for m in re.finditer('[a-zA-Z`\_]+[0-9]*', code):
            yield m.group()

    c1 = regex_iter(code1)
    c2 = regex_iter(code2)
    
    subs = set((src, dst) for src, dst in zip(c1, c2) if src != dst)
        
    # convert the substitituions to a list so we can append to it
    subs = list(subs)
        
    PLACEHOLDER = '`'

    current = code1
    for i, (f, r) in enumerate(subs):
        
        # if we're on the first possible substitution, we remove the find
        # value and put in a placeholder for the replace value. this
        # handles circular substitutions. e.g. if the user wants to swap
        # "A" and "B" they would do: "A" -> "C", "B" -> "A", "C" -> "A"
        if not i:
            subs.append((PLACEHOLDER, r))
            r = PLACEHOLDER

        # start with an empty string a pointer to the head of temp
        temp, p = '', 0
        
        # for each item that might be a variable name
        for m in re.finditer(pattern='[a-zA-Z`\_]+[0-9]*', string=current):

            # if the potential variable name is the one we're removing
            if m.group() == f:

                # add in everything from the pointer up to the start of
                # the found name and then use the subsituted name instead
                temp += current[p: m.start()] + r

                # move the pointer to the end of the name in temp
                p = m.end()
                
        # add whatever is left that we didn't replace from temp
        temp += current[p:]

        # this substitution is finished, so save the value as current
        current = temp

    # after all the substitutions, do the strings match?
    return current == code2

