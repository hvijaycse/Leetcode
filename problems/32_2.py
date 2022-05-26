
from typing import List, Optional, Any, Dict



class Solution:
    def longestValidParentheses(self, s: str) -> int:

        ParanStack = [-1]
        maxLen = 0

        for index, char in enumerate(s):

            if char == '(':
                ParanStack.append(index)
            else:
                ParanStack.pop()

                if not ParanStack:
                    ParanStack.append(index)
                else:
                    maxLen = max(maxLen, index - ParanStack[-1])
        return maxLen