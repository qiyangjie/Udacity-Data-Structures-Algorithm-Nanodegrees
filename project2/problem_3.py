import sys
from collections import Counter
import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def is_leaf_node(self):
        return self.left is None and self.right is None

    def __add__(self, other):
        new_node = Node(None, self.freq + other.freq)
        new_node.left = self
        new_node.right = other
        return new_node

    def __lt__(self, other):
        if other is None:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.freq < other.freq

    def __repr__(self):
        return "('{}', {})".format(self.char, self.freq)


class Tree:
    def __init__(self, node):
        self.root = node

    def get_root(self):
        return self.root


def pre_order(root_node):
    code = ''
    huffman_dict = dict()

    def traverse(node, current_code):

        if node:
            if node.is_leaf_node():
                huffman_dict[node.char] = current_code
            else:
                # traverse left subtree
                left_code = current_code + '0'
                traverse(node.left, left_code)

                # traverse right subtree
                right_code = current_code + '1'
                traverse(node.right, right_code)

    traverse(root_node, code)

    return huffman_dict


def huffman_encoding(data):
    # 1. Determine the frequency of each character in the message
    # Counter is a subclass of dict
    char_counter = Counter(data)
    # 2. Sort by frequency from least common
    char_list = char_counter.most_common()[::-1]
    # create the node list
    node_heapq = []
    for (char, freq) in char_list:
        heapq.heappush(node_heapq, Node(char, freq))

    # add to list and sort
    while len(node_heapq) > 1:
        # 3 and 4 Pop-out two nodes with mini frequency and configure new nodes
        new_node = heapq.heappop(node_heapq) + heapq.heappop(node_heapq)
        # Make our list work as a priority queue
        heapq.heappush(node_heapq, new_node)

    huffman_tree = Tree(node_heapq.pop())
    huffman_dict = pre_order(huffman_tree.get_root())

    encode_data = ''
    for char in data:
        encode_data += huffman_dict[char]

    return encode_data, huffman_tree


def huffman_decoding(data, tree):
    decode = ''
    current_node = tree.get_root()
    for bit in data:
        if bit is '0':
            if current_node.left is None:
                decode += current_node.char
                current_node = tree.get_root()

            current_node = current_node.left

        if bit is '1':
            if current_node.right is None:
                decode += current_node.char
                current_node = tree.get_root()

            current_node = current_node.right

    decode += current_node.char

    return decode


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
