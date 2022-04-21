from typing import List, Optional, Any, Dict


class Node:

    def __init__(self, val: int, next = None, prev = None) -> None:
        self.val = val
        self.next: Node = next
        self.prev: Node = prev
    



class MyHashSet:

    def __init__(self):
        self.m: int = 10000
        self.array: List[Node] = [None for _ in range(self.m)]

    def add(self, key: int) -> None:

        mod = key % self.m
        new_node = Node(key, self.array[mod])
        if self.array[mod]:
            self.array[mod].prev = new_node
        self.array[mod] = new_node

    def remove(self, key: int) -> None:
        mod = key % self.m
        current_node = self.array[mod]

        while current_node:
            if current_node.val == key:

                previous = current_node.prev
                following = current_node.next

                if previous:
                    previous.next = following
                else:
                    self.array[mod] = following
                if following:
                    following.prev = previous
            current_node = current_node.next
                
        

    def contains(self, key: int) -> bool:
        
        mod = key % self.m
        current_node = self.array[mod]

        while current_node:
            if current_node.val == key:
                return True
            current_node = current_node.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)