class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        chars = {}
        for char in s1:
            if char in chars:
                chars[char]+=1
            else:
                chars[char]=1

        windows = {}
        for right in range(len(s2)):
            if s2[right] in windows:
                windows[s2[right]]+=1
            else:
                windows[s2[right]] = 1

            if right - left == len(s1)-1:
                if windows == chars:
                    return True
                windows[s2[left]]-=1
                if windows[s2[left]] == 0:
                    del windows[s2[left]]
                left +=1


        return False




           