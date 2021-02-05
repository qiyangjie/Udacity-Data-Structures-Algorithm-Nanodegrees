class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


def union(llist_1, llist_2):
    # Your Solution Here
    # Make the first list as the ordered list

    # Read the value of llist to a python list.
    union_list = []
    current_node = llist_1.head
    while current_node:
        union_list.append(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        union_list.append(current_node.value)
        current_node = current_node.next

    # remove the duplications
    union_list = list(set(union_list))

    # Configure the output as linked list
    output_list = LinkedList()
    for value in union_list:
        output_list.append(value)

    return output_list


def intersection(llist_1, llist_2):
    list_1 = []
    list_2 = []

    current_node = llist_1.head
    while current_node:
        list_1.append(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        list_2.append(current_node.value)
        current_node = current_node.next

    list_1 = set(list_1)
    list_2 = set(list_2)

    list_3 = [value for value in list_1 if value in list_2]

    # Configure the output as linked list
    output_list = LinkedList()
    for value in list_3:
        output_list.append(value)
    return output_list


if __name__ == '__main__':
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
