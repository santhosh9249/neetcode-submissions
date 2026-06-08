class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for n in range(len(nums)):
            difference = target - nums[n]
            if difference in hashmap:
                return [ nums.index(difference), n]
            hashmap[nums[n]] =  1 + hashmap.get(nums[n], 0)
            