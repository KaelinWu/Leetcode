class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False


        hand.sort()
        count = Counter(hand)
        
        print(hand)
        total_hands = 0
        for num in hand:
            if count[num]:
                for k in range(groupSize):
                    if count[num+k] == 0:  
                        return False
                    count[num+k] -= 1
                
        return True

    #1,2,4,2,3,5,3,4
    #1,2,2,3,3,4,4,5