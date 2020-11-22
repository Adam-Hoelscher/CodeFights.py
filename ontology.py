from collections import namedtuple


def ontology(treeRepr, questions, queries):
    
    Node = namedtuple('Node', ['name', 'children', 'questions'])

    root_name, *descendants = treeRepr.split(' ')
    root = Node(root_name, [], [])
    index = {root_name: root}
    trees = [root]

    prior = []
    for k in descendants:
        if k == '(':
            prior.append(trees)
            trees = trees[-1].children
        elif k == ')':
            trees = prior.pop()
        else:
            child = Node(k, [], [])
            trees.append(child)
            index[k] = child
            
    for q in questions:
        k, v = q.split(': ')
        index[k].questions.append(v)

    def search(tree, words):
        temp = sum(q.startswith(words) for q in tree.questions)
        temp += sum(search(t, words) for t in tree.children)
        return temp

    ans = []
    for q in queries:
        topic, *words = q.split(' ')
        words = ' '.join(words)
        ans.append(search(index[topic], words))
        
    return ans
