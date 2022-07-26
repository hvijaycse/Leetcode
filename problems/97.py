from functools import lru_cache
from typing import List, Optional, Any, Dict
from timeDec import timeit
import time

class Solution:
    @lru_cache(None)
    # @timeit
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # print(s1, s2, s3)
        if len(s1) == len(s2) == len(s3) == 0:
            return True
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        if len(s1) == 0 :
            return s2 == s3
        
        elif len(s2) == 0:
            return s1 == s3
        
        if s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:]):
            return True
        if s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]):
            return True


        return False

# print(Solution().isInterleave("aabcc", "dbbca", "dbbca"))
# print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))

print(Solution().isInterleave(
    "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
    "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
    "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
))

