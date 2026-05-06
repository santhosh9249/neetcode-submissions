class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
      var1 = sorted(s)
      var2 = sorted(t)
      if var1 == var2:
        return True
      else:
        return False
      
        

        