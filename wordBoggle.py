# from collections import defaultdict
from itertools import product

def wordBoggle(board, words):

    word_dict = {}
    for w in words:
        v = word_dict
        while w[0] in v:
            v = v[w[0]]
            w = w[1:]
        while w:
            v[w[0]] = {}
            v = v[w[0]]
            w = w[1:]
            
    letters = {}
    for i, row in enumerate(board):
        for j, l in enumerate(row):
            letters[(i,j)] = l
    
    def chain_get(word):
        v = word_dict
        while word:
            v = v[word[0]]
            word = word[1:]
        return v
    
    def search(i, j, path=[], word=''):
        if word in words:
            print('found', word, path)
            answers.add(word)
        else:
            l = letters.get((i, j))
            path += [(i, j)]
            w = chain_get(word)
            if l in w:
                for ic, jc in product(*([[-1,0,1]]*2)):
                    new_pos = i + ic, j + jc
                    if new_pos not in path:
                        search(*new_pos, path, word + l)
    
    answers = set()
    for (i, j) in letters:
        search(i, j)
        
    return sorted(answers)
