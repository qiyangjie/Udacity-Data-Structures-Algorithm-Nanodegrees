Project 2 explanation

Problem 1 LRU Cache

The LRU data structure should:
1) memory address is the key, memory content is the value\
   -> key:value pair -> dictionary
2) The entry is preserved by access order. -> ordered dictionary

Time complexity:
1) get function()\
   a. in operation -> O(1)\
   b. move_to_end()-> O(1)\
   c. overall -> O(1)

2) set function()\
   a. insert operation -> O(1)\
   b. move_to_end()-> O(1)\
   c. popitem()->O(1)\
   d. overall->O(1)
   
Problem 2
   