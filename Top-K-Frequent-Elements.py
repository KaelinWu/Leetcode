class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for number in nums:
            mp[number] += 1
        
        sorted_data = list(sorted(mp.items(), key=lambda item: item[1], reverse=True))

# Convert the sorted list back to a dictionary (if needed)
        print(sorted_data)
        numbers = list()
        for idex in range(k):
            numbers.append(sorted_data[idex][0])

        return numbers
            
            
        
        
        

