from typing import List, Optional

def int_input()-> int:
    '''used for integer input'''
    return(int(input()))

def list_input( seperator: str = ' ')-> List:
    '''used for list input in a line seperated by seperator'''
    return input().split(seperator)

def int_list_input(seperator: str = ' ') -> List[int]:
    '''Used to get integer list in a line'''
    return list( map(int, list_input(seperator)))


class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = [ 0 for _ in range(self.size) ]
        

    def fix(self, idx: int) -> None:
        self.bits[idx] = 1

    def unfix(self, idx: int) -> None:
        self.bits[idx] = 0

    def flip(self) -> None:
        
        for index in range(self.size):
            self.bits[index] ^= 1
        
    def all(self) -> bool:
        item = 1
        for bit in self.bits:
            item &= bit
            if not item:
                return False
        return True
    
    def one(self) -> bool:
        item = 0
        for bit in self.bits:
            item |= bit
        
        if item:
            return True
        else:
            return False
        

    def count(self) -> int:
        count = 0 
        for bit in self.bits:
            if bit:
                count += 1
        return count
        

    def toString(self) -> str:
        ans = ''
        
        for bit in self.bits:

            if bit:
                ans += '1'
            else:
                ans += '0'
        return ans


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()