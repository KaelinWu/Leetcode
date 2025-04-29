class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mymap = {
            '2': \abc\, 
            '3':\def\, 
            '4':\ghi\, 
            '5':\jkl\, 
            '6':\mno\, 
            '7':\pqrs\, 
            '8':\tuv\, 
            '9':\wxyz\
            }
        result = []
    
        def helper(next_digits, combination):
            if len(next_digits) == 0:
                return result.append(combination)
            else:
                for char in mymap[next_digits[0]]:
                    helper(next_digits[1:], combination + char)
            
        combinations = \\
        helper(digits, combinations)
        return result

        


        