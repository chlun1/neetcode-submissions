class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def helper(s):
            #print(f"helper: {s}")
            if len(s) == 0:
                return True		
    
            if s in cache:
                return cache[s]
    
            res = False
    
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    #print(s[:i+1])
                    if helper(s[i+1:]):
                        res = True
                        break
    
            cache[s] = res
            return res
    
        return helper(s)
            