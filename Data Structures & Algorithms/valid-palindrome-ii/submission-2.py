class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()

        def helper(l, r, deleted):
            if l > r:
                return True

            if not s[l].isalnum():
                return helper(l + 1, r, deleted)
            if not s[r].isalnum():
                return helper(l, r - 1, deleted)
    
            if s[l] != s[r]:
                if deleted:
                    return False
                if helper(l + 1, r, True):
                    return True
                elif helper(l, r - 1, True):
                    return True
                else:
                    return False
            
            return helper(l + 1 , r - 1, deleted)

        return helper(0, len(s) - 1, False)
        