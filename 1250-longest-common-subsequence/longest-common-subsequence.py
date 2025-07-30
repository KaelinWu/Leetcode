class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        if len(text2) > len(text1):
            text1, text2 = text2, text1
            
        
        prev = [0] * (len(text2)+1)

        for i in range(len(text1)):
            dp = [0] * (len(text2)+1)
            for j in range(1,len(text2)+1):
                if text1[i] == text2[j-1]:
                    
                    dp[j] = prev[j-1] + 1
                else:
                    dp[j] = max(dp[j-1],prev[j])
            prev = dp
        return prev[-1]
