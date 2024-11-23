class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls_set = set(map(tuple, walls))
        guards_set = set(map(tuple, guards))
        
        guarded = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
        for r, c in guards_set:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if (nr, nc) in walls_set or (nr, nc) in guards_set:
                        break
                    guarded.add((nr, nc))
                    nr += dr
                    nc += dc
        
        total_cells = m * n
        occupied_cells = len(walls_set) + len(guards_set) + len(guarded)
        return total_cells - occupied_cells