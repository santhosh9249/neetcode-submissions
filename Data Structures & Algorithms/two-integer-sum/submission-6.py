class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
          for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
              return [i,j]
            

          
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevMap = {} # val : index

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i


# The enumerate() function is a built-in Python tool that makes it easy to keep track of the index (position) of an item while you are looping through a list (or any iterable).

# Without enumerate(), if you wanted both the index and the value, you’d have to write something clunky like this: