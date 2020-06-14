"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
 

Note: You may assume the string contain only lowercase English letters.

Note: collections.OrderedDict will be required for py < 3.7, but py > 3.7 has ordereddict as a default
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = collections.OrderedDict()
        for char in list(s):
            try:
                hashmap[char]
            except KeyError:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        non_repeat = None
        for k,v in hashmap.items():
            if v == 1:
                non_repeat = k
                break
        if not non_repeat:
            return -1
        return list(s).index(non_repeat)
        
        
