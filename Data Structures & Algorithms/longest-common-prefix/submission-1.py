class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        res = 0
        stop = False
        for i in range(min_len):
            c = strs[0][i]
            for s in strs[1:]:
                if s[i] != c:
                    stop = True
                    break
            if stop:
                break
            res += 1
        
        return strs[0][:res]
        