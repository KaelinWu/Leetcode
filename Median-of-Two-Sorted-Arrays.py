class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len(B):
            A,B = B,A
        
        total = len(A) + len(B)
        half = total // 2
        l = 0
        r = len(A)-1
        while True:
            i = (l+r) //2
            j = half - i -2

            Aind = A[i] if i>= 0 else float(\-inf\)
            Aright = A[i+1] if i+1 < len(A) else float(\inf\)
            Bind = B[j] if j>= 0 else float(\-inf\)
            Bright = B[j+1] if j+1 < len(B) else float(\inf\)

            if Aright >= Bind and Bright >= Aind:
              
                if total %2:
                    return min(Aright,Bright)
                return (max(Aind,Bind) + min(Aright,Bright))/2
            
            if Aind > Bright:
                r = i -1
            else:
                l = i +1

        
        # 13567
        # 23458910

        # 1233455678910
        # 5
