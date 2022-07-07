from typing import List, Optional, Any, Dict


class Node:

    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class FreqStack:

    def __init__(self):

        # This is used to count the 
        # frequency of the elements
        self.frequency_count = dict()

        # This is used to maintain the 
        # element of frequency

        self.frequency_stack = dict()

        #this is used to maintain 
        # the max frequency
        self.max_frequency = 0
        

    def push(self, val: int) -> None:

        new_node = Node(val, None)

        if val not in self.frequency_count:
            self.frequency_count[val] = 0

        self.frequency_count[val] += 1

        frequency = self.frequency_count[val] 

        if frequency not in self.frequency_stack:
            self.frequency_stack[frequency] = new_node
        
        else:
            new_node.next = self.frequency_stack[frequency]
            self.frequency_stack[frequency] = new_node
        
        self.max_frequency = len(self.frequency_stack)

    def pop(self) -> int:

        max_node: Node = self.frequency_stack[self.max_frequency]
        self.frequency_count[max_node.val] -= 1

        if max_node.next is None:
            del self.frequency_stack[self.max_frequency]
        else:
            self.frequency_stack[self.max_frequency] = max_node.next
        
        self.max_frequency = len(self.frequency_stack)

        return max_node.val
                 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
