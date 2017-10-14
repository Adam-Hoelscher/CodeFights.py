def findSubstrings(words, parts):

    strings_of_length = dict()

    def add_to_tree(t, val):
        if len(val) == 1:
            t[val[0]] = False
        else:
            if val[0] not in t: t[val[0]] = dict()
            next_t = t[val[0]]
            add_to_tree(next_t, val[1:])

    for p in parts:
        l = len(p)
        if l not in strings_of_length: strings_of_length[l] = dict()
        add_to_tree(strings_of_length[l], p)

    def check(string, tree, top = True):

        if not string: return(False)
        if string[0] not in tree: return(False)

        if top:
            temp = '['
        else:
            temp = ''

        next_tree = tree[string[0]]
        if next_tree:
            next_check = check(string[1:], next_tree, False)
            if not next_check: return(False)
            temp += (string[0] + next_check)
        else:
            temp += (string[0] + ']' + string[1:])

        return(temp)

    for l in sorted(strings_of_length.keys(), reverse=True):
        for word_pos, word in enumerate(words):
            if '[' not in word:
                for letter_pos, letter in enumerate(word):
                    new_end = check(word[letter_pos:], strings_of_length[l])
                    if new_end:
                        words[word_pos] = word[:letter_pos] + new_end
                        break

    return(words)
