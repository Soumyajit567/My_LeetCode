class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M = len(grid)
        N = len(grid[0])
        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()
        visited = set()
        res = [0 for i in range(len(queries))]
        minHeap = [(grid[0][0], 0 , 0)]
        points = 0
        visited.add((0,0))
        directions = [(-1, 0),(0, -1), (1, 0), (0, 1)]
        for limit, idx in q:
            while minHeap and minHeap[0][0] < limit:
                val, r, c = heapq.heappop(minHeap)
                points += 1
                for dx, dy in directions:
                    dr = dx + r
                    dc = dy + c
                    if 0 <= dr < M and 0 <= dc < N and (dr,dc) not in visited:
                        heapq.heappush(minHeap,(grid[dr][dc], dr, dc))
                        visited.add((dr,dc))
            res[idx] = points
        return res