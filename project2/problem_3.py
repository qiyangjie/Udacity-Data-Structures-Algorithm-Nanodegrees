import sys
import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if other is None:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.freq < other.freq


def huffman_encoding(data):
    # Phase I: Build huffman tree
    encode_tree = []
    # 1.1 Determine the frequency of each char
    character_list = dict()
    for character in data:
        if character in character_list:
            character_list[character] += 1
        else:
            character_list[character] = 1

    for key in character_list:
        node = Node(key, character_list[key])
        heapq.heappush(encode_tree, node)

    while len(encode_tree) > 1:
        node1 = heapq.heappop(encode_tree)
        node2 = heapq.heappop(encode_tree)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(encode_tree, merged)

    # Make codes

    print('End!')

    # sorted_character = sorted(character_list.items(), key=lambda kv: (kv[1], kv[0]))
    # print(sorted_character)
    #
    # for i in range(len(sorted_character) - 1):
    #
    #     if i == 0:
    #         left = sorted_character.pop(0)
    #         right = sorted_character.pop(0)
    #         value = left[1] + right[1]
    #     else:
    #         left = node_temp
    #         right = sorted_character.pop(0)
    #         value = left.get_value() + right[1]
    #         print(value)
    #
    #     node_temp = Node()
    #     node_temp.set_value(value)
    #     node_temp.set_left_child(left)
    #     node_temp.set_right_child(right)
    #
    # encode_tree = Tree(node_temp)

    return encode_tree


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    test = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    result = huffman_encoding(test)

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}\n".format(decoded_data))
