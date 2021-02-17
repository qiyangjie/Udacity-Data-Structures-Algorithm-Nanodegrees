import hashlib
import datetime


def calc_hash():
    sha = hashlib.sha256()

    hash_str = "We are going to encode this string of data!".encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest()


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash()
        self.next = None

    def __repr__(self):
        return "time:{}\n" \
               "data:{}\n" \
               "hash:{}\nn" \
               "previous_hash: {}\n".format(self.timestamp, self.data, self.hash, self.previous_hash)


class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, value=None):
        if self.head is None:
            self.head = Block(value, 0)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Block(value, node.hash)


if __name__ == '__main__':
    # Test 1
    myChain = BlockChain()
    myChain.append("information 1")
    myChain.append("information 2")
    myChain.append("information 3")

    print(myChain.head)
    print(myChain.head.next)
    print(myChain.head.next.next)

    # Test 2
    myChain = BlockChain()
    myChain.append()
    myChain.append("information 2")
    myChain.append("information 3")

    print(myChain.head)
    print(myChain.head.next)
    print(myChain.head.next.next)

    # Test 3
    myChain = BlockChain()
    myChain.append()
    myChain.append()
    myChain.append()

    print(myChain.head)
    print(myChain.head.next)
    print(myChain.head.next.next)

