class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []

        def create_set(start, subset):
           
             
            for i in range(start, len(nums)):
               
                create_set(i+1, subset + [nums[i]])
                
            power_set.append(subset)
        
            

        create_set(0,[])
                
        return power_set
                


        


        
        
            