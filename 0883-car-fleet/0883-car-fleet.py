class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of (position, time to reach target) tuples and sort by farthest to nearest
        cars = sorted(zip(position, [(target - p) / s for p, s in zip(position, speed)]))
        
        fleets = 0
        cur_time_to_target = 0
        
        # Go through the list of cars from the one nearest to the target to the farthest
        for _, time in reversed(cars):
            # If the current car's time to reach the target is more than the current
            # time to target (i.e., it's not catching up to the fleet ahead), it starts a new fleet
            if time > cur_time_to_target:
                fleets += 1
                cur_time_to_target = time
        
        return fleets





# Wrong
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == len(speed) == 1:
            return 1
        else:
            stack = []
            hashmap = {}
            for i in range(len(position)):
                val = position[i] + speed[i]
                if val < target and val not in hashmap:
                    hashmap[val] = 0
                if val >= target and val not in hashmap:
                    hashmap[val] = 1
                if stack and val == stack[-1] and val in hashmap:
                    stack.pop()
                    hashmap[val] += 1
                stack.append(val)
            res = 0
            for key, count in hashmap.items():
                res += count
            return res if res > 1 else 1
"""
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        
        # Create pairs of position and speed for each car
        for x in range(len(speed)):
            pairs.append([position[x], speed[x]])
        
        # Sort the pairs based on position in descending order
        pairs = sorted(pairs)[::-1]
        
        # Iterate through the sorted pairs
        for p, s in pairs:
            # Calculate time to reach the target for the current car
            time = (target - p) / s
            
            # Add the time to the stack
            stack.append(time)
            
            # Check if there are at least two cars in the stack and the current car
            # takes less or equal time than the previous car. If so, pop the previous car.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # The length of the stack represents the number of car fleets
        return len(stack)

        

"""