from typing import List, Optional, Any, Dict


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        

        mapping = {
            ' '  : ' ' 
        }

        character = 97

        for char in key:
            
            if char not in mapping and char != ' ':
                mapping[char] = chr(character)
                character += 1
        
        output = ''
        
        for char in message:
            output += mapping[char]
        
        return output

