import sys
from collections import Counter

from problem_3 import Node, Tree, pre_order, huffman_decoding


def huffman_encoding_1(data):
    # 1. Determine the frequency of each character in the message
    # Counter is a subclass of dict
    char_counter = Counter(data)
    # 2. Sort by frequency from least common
    char_list = char_counter.most_common()[::-1]
    # create the node list
    node_list = [Node(char, freq) for (char, freq) in char_list]

    # add to list and sort
    while len(node_list) > 1:
        # 3 and 4 Pop-out two nodes with mini frequency and configure new nodes
        new_node = node_list.pop(0) + node_list.pop(0)
        # Make our list work as a priority queue
        node_list.append(new_node)
        node_list.sort()

    huffman_tree = Tree(node_list.pop(0))
    huffman_dict = pre_order(huffman_tree.get_root())

    encode_data = ''
    for char in data:
        encode_data += huffman_dict[char]

    return encode_data, huffman_tree


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding_1(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

