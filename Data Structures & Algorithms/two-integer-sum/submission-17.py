class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()
        for n in range(len(nums)):
            difference = target - nums[n]
            if difference in hashset:
                return [ nums.index(difference), n]
            hashset.add(nums[n])
            