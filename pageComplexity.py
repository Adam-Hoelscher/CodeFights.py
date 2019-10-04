from html.parser import HTMLParser


class deepParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        super(deepParser, self).__init__()
        self.tags = {}
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        self.depth += 1
        if self.depth not in self.tags:
            self.tags[self.depth] = set()
        self.tags[self.depth].add(tag)

    def handle_endtag(self, tag):
        self.depth -= 1
    
    def answer(self):
        max_depth = max(self.tags.keys())
        return self.tags[max_depth]

    
def pageComplexity(document):

    tree = deepParser()
    tree.feed(document)

    return sorted(list(tree.answer()))
