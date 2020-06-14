"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s.strip()) == 0: return True
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s.lower())
        left = 0
        right = len(s) -1 
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right -1
        return True
        
            
        
