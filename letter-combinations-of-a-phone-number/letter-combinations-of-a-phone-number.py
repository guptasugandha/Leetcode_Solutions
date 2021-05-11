class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def recursive(i=0, combo="", res=[]):
            if i == len(digits):
                res.append(combo)
            else:
                nextDigit = digits[i]
                children = d[nextDigit]
                for child in children:
                    recursive(i+1, combo+child, res)
            
            return res
        
        return recursive(0, "", [])