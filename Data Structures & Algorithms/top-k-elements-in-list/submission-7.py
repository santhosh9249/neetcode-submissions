class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap= {}
        ls= []
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i],0)                
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        ls=[]
        for i in range(k):
             ls.append(sorted_items[i][0])
        return ls