"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        int_val = 0
        for idx, val in enumerate(digits):
            if idx == len(digits):
                int_val += 1*val
            else:
                int_val += pow(10,(len(digits)-idx-1)) * val
        int_val += 1
        
        int_val_str = str(int_val)
        digits_str = [int(char) for char in int_val_str]
        
        return digits_str
