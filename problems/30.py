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
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if not s or not words:
            return []
        
        words_no = len(words)
        word_len = len(words[0])
        words_len = word_len * words_no
        n = len(s)
        word_dict = {}
        indexes = []

        for word in words:
            word_dict[word] = word_dict.get(word, 0 ) + 1


        for index in range(n - words_len + 1):
            temp_dict = word_dict.copy()
            word_count = 0
            for i in range(index, index + words_len, word_len):
                item = s[i: i+word_len]

                if item not in temp_dict:
                    break

                if temp_dict[item] > 0 :
                    temp_dict[item] -= 1
                    word_count += 1
                else:
                    break

            if word_count ==  words_no:
                indexes.append(index)
        return indexes
