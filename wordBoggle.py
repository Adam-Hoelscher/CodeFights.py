from itertools import product

def wordBoggle(board, words):

    words = set(words)

    stems = set()
    for w in words:
        hold = ''
        for l in w:
            hold += l
            stems.add(hold)
    
    letters = {}
    for i, row in enumerate(board):
        for j, l in enumerate(row):
            letters[(i,j)] = l
    
    def search(i, j, path=[], word=''):
        
        if word in words:
            answers.add(word)
            
        for ic, jc in product(*([[-1,0,1]]*2)):
            new_pos = i + ic, j + jc
            l = letters.get(new_pos)
            if l and new_pos not in path:
                new_word = word + l
                if new_word in stems:
                    search(*new_pos, path + [new_pos], new_word)

    answers = set()
    for k, v in letters.items():
        search(*k, [*k], v)

    return sorted(answers)
