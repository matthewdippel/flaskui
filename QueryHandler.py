class QueryHandler:

    def handle(self, string):
        raise NotImplementedError()

class QueryCharCountHandler(QueryHandler):
    def __init__(self):
        return

    def handle(self, string):
        from collections import Counter
        c = Counter(string)
        def fix(x):
            if x == ' ':
                return '" "'
            return x
        output = "<br/>".join(["%s : %d" % (fix(x), c[x]) for x in sorted(c.keys())])
        return output
