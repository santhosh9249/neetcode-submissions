class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            sorts = ''.join(sorted(strs[i]))
            if sorts in hashmap:
                hashmap[sorts].append(strs[i])
            else:
                hashmap[sorts]= [strs[i]]
        return list(hashmap.values())


