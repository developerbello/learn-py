class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        total = 0
        
        if len(nums) == 0:
          return -1
        
        for num in range(0, len(nums)):
          for num2 in range(0, len(nums)):

            if num == num2:
              continue
            total = nums[num] + nums[num2]
                
            if total is not target:
              continue
            else:
              return [num, num2]
