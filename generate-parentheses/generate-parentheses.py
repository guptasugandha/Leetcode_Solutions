class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(s,opening,closing):
            if len(s) == 2*n:
                ans.append("".join(s))
                return
            
            if opening == closing or opening < n:
                s.append("(")
                generate(s,opening+1,closing)
                s.pop()

            if opening > closing and closing < n:
                s.append(")")
                generate(s,opening,closing+1)
                s.pop()
            
        
        s = []
        ans = []
        generate(s,0,0)
        
        return ans