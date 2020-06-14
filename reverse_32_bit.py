"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = True if x < 0 else False
        int_str = list(str(abs(x)))
        
        left = 0
        right = len(int_str)-1
        while left < right:
            int_str[left], int_str[right] = int_str[right], int_str[left]
            left, right = left+1, right-1
            
        int_val = int("".join(int_str))
        # upper bound of a signed integer is not 232 - 1, but 231 - 1, since the first bit is the sign bit.
        if int_val>>31:
            return 0
        return -1 * int_val if is_neg else int_val
        
        
