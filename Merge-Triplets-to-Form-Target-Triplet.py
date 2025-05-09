class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        
            
            
        found = [False] * 3
        
        for tripple in triplets:
            if tripple[0] == target[0] and tripple[1] <= target[1] and tripple[2] <= target[2]:
                found[0] = True
            if tripple[1] == target[1] and tripple[2] <= target[2] and tripple[0] <= target[0]:
                found[1] = True
            if tripple[2] == target[2] and tripple[1] <= target[1] and tripple[0] <= target[0]:
                found[2] = True
        return found[0] and found[1] and found[2]



        
