from typing import List, Optional, Any, Dict

class Node:

    def __init__(self, value, minimum) -> None:
        
        self.value = value
        self.minimum = minimum
        self.next = None
    
    def set_next(self, next: 'Node'):
        self.next = next
    
    def get_next(self,):
        return self.next
    
    def get_minimum(self,):
        return self.minimum
    
    def get_value(self, ):
        return self.value




class MinStack:

    def __init__(self):
        self.head = None
        

    def push(self, val: int) -> None:

        if not self.head:
            self.head = Node(value=val, minimum=val)
        
        else:
            current_min = self.head.get_minimum()
            if val < current_min:
                current_min = val
            
            temp = Node(value=val, minimum=current_min)
            temp.set_next(self.head)

            self.head = temp
        

    def pop(self) -> None:
        self.head = self.head.get_next()
        
    def top(self) -> int:
        return self.head.get_value()

    def getMin(self) -> int:
        return self.head.get_minimum()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
