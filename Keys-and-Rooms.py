class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]
        visited_rooms = [False for _ in range(len(rooms))]
        while keys:
            key = keys.pop()
            if not visited_rooms[key]:
                visited_rooms[key] = True
                for new_key in rooms[key]:
                    keys.append(new_key)
        
        if (all(visited_rooms)):
            return True
        
        else:
            return False