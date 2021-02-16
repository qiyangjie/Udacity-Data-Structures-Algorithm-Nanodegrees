Project 2 explanation

Problem 1 LRU Cache

The LRU data structure should:
1) memory address is the key, memory content is the value\
   -> key:value pair -> dictionary
2) The entry is preserved by access order. -> ordered dictionary


1) get function()\
   Time complexity:\
   a. in operation -> O(1)\
   b. move_to_end()-> O(1)\
   c. overall -> O(1)
   
   Space complexity: O(n)
   

2) set function()\
   Time complexity:\
   a. insert operation -> O(1)\
   b. move_to_end()-> O(1)\
   c. popitem()->O(1)\
   d. overall->O(1)
   
   space complexity: O(n)
   
Question:
1. Any better data structure should I use?
   
Problem 2

The only idea I have for this question is go through all the directories
and find all qualified files.

The time complexity is O(n), space complexity is O(n)

Question:
1. Is there any better data structure or algorithm should I use?


Problem 3

For this problem , I just follow the instruction provided. 
1. Huffman encode\
   a. I utilized Counter to preserve each character, as it is efficient to sort by frequency O(n log n).\
   b. Create the node list using heapq, heapq push and pop are O(log n)\
   c. Store all element to heapq. -> O(n log n)\
   d. The time complexity of pre-order traversal is O(n)
   e. Overall time complexity is O(n log n)
   f. Overall space complexity is O(n)
   
2. Huffman decode
   a. Traverse the tree to decode. Time complexity is O(n).
   b. Space complexity is O(n).



Problem 4

I go through all sub-groups to find whether a user in.

The time complexity is O(n), Space complexity is O(n).

Question:
1. Is there any better data structure or algorithm should I use?

Problem 5

The question looks like implementing a linked list.
Is this what I should do?

The time complexity for append function is O(n), 
The space complexity for append function is O(n)/

Question:
1. If the blockchain use a linked list, 
   when there are many nodes in the chain, 
   even add a node use significant time. 
   Why a linked list is used here? 
   We have better choices, isn't it?
   

Problem 6:
1. Union Function\
   a. Read all element from linked list 1 to union list. O(n)\
   b. Read all element from linked list 2 to union list. O(n)\
   c. Remove duplications by convert list to set. O(n)\
   d. Convert set to linked list and output. O(n)\
   e. Overall time complexity is O(n)\
   f. Overall space complexity is O(4n)->O(n)

2. Intersection Function\
   a. Read all element from linked list 1 to list 1. O(n)\
   b. Read all element from linked list 2 to list 1. O(n)\
   c. Remove duplications by convert list to set. O(n)\
   d. Iterate elements in list 1, check whether it is in list 2. O(n^2)\
   e. Transfer list to linked list. O(n)\
   f. Overall time complexity is O(n^2)\
   g. Overall space complexity is O(5n)->O(n)
   
Question:
   1. Is convert list to set is a proper method to remove duplication?
   2. Is there any better way to do those functions?
   