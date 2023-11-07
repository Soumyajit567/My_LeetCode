class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        # Calculate time to reach the city for each monster
        time_to_city = [(dist[i] / speed[i]) for i in range(n)]
        
        # Sort monsters by their time to reach the city
        time_to_city.sort()
        
        # Iterate through the sorted list and see how many you can eliminate
        monsters_eliminated = 0
        for time in time_to_city:
            # If the time is greater than the monsters eliminated, you can eliminate this one too
            if time > monsters_eliminated:
                monsters_eliminated += 1
            else:
                # A monster reaches the city before or at the same time you can fire, game over
                break
        
        return monsters_eliminated