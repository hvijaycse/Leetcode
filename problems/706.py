from typing import List, Optional, Any, Dict



class Node:

    def __init__(self, key:int, val: int, next = None, prev = None) -> None:
        self.key = key
        self.val = val
        self.next: Node = next
        self.prev: Node = prev
    

class MyHashMap:

    def __init__(self):
        self.m: int = 10000
        self.array: List[Node] = [None for _ in range(self.m)]  

    def put(self, key: int, value: int) -> None:
        mod = key % self.m
        new_node = Node(key, value, self.array[mod])
        if self.array[mod]:
            self.array[mod].prev = new_node
        self.array[mod] = new_node


    def get(self, key: int) -> int:
        mod = key % self.m
        current_node = self.array[mod]

        while current_node:
            if current_node.key == key:
                return current_node.val
            current_node = current_node.next
        
        return -1


    def remove(self, key: int) -> None:
        mod = key % self.m
        current_node = self.array[mod]

        while current_node:
            if current_node.key == key:

                previous = current_node.prev
                following = current_node.next

                if previous:
                    previous.next = following
                else:
                    self.array[mod] = following
                if following:
                    following.prev = previous
            current_node = current_node.next
                
