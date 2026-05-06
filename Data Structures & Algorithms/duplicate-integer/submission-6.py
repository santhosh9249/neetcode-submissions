class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      flag=0
      for i in nums:
        var = nums.count(i)
        if var > 1:
          flag=1
          break
      if flag==1:
        return True
      else:
        return False
