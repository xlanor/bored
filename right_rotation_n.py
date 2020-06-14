"""
iven an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0

"""
class Solution(object):
    def gcd(self,a, b):
        if a == 0 : 
            return b  

        return self.gcd(b%a, a) 
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # No need to do anything if k is 0,
        if k == 0:
            return 
        if len(nums) == 0 or len(nums) == 1:
          return
        set_nums = self.gcd(len(nums),k)
        temp = 0
        for set_no in range(set_nums):
            temp = nums[set_no]
            cur_idx = set_no
            while True:
                next_idx = cur_idx + k
                while next_idx >= len(nums):
                    next_idx -= len(nums)
                if next_idx == set_no:
                    nums[next_idx] = temp
                    break
                else:
                    temp2 = nums[next_idx]
                    nums[next_idx] = temp
                    temp = temp2
                    cur_idx = next_idx
