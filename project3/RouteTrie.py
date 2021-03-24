from collections import defaultdict


class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, part, handler):
        self.children[part] = RouteTrieNode(handler)


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root
        for part in parts:
            current = current.children[part]

        current.handler = handler

    def find(self, prefix):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if not prefix:
            return self.root.handler

        node = self.root
        for part in prefix:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, _handler, _none_handler):
        self.route_trie = RouteTrie(_handler)
        self.none_handler = _none_handler

    def add_handler(self, path, handler):
        parts = self.split_path(path)
        self.route_trie.insert(parts, handler)

    def lookup(self, path):
        parts = self.split_path(path)
        return self.route_trie.find(parts)

    @staticmethod
    def split_path(path):
        if path == "/":
            return

        parts = path.split('/')
        parts.remove('')
        return parts


if __name__ == '__main__':
    # Here are some test cases and expected outputs you can use to test your implementation

    # create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
