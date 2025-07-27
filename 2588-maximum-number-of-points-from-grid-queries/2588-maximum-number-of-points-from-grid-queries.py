class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M, N = len(grid), len(grid[0])
        parent = {}   # Union-Find parent
        size = {}     # Size of each component
        result = [0] * len(queries)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return
            if size[xr] < size[yr]:
                xr, yr = yr, xr
            parent[yr] = xr
            size[xr] += size[yr]

        # Flatten and sort grid cells by value
        cells = [(grid[r][c], r, c) for r in range(M) for c in range(N)]
        cells.sort()

        # Sort queries and track original indices
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        visited = [[False] * N for _ in range(M)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        cell_idx = 0
        for q, qi in sorted_queries:
            # Add all cells < q into union-find
            while cell_idx < len(cells) and cells[cell_idx][0] < q:
                val, r, c = cells[cell_idx]
                idx = r * N + c
                parent[idx] = idx
                size[idx] = 1
                visited[r][c] = True
                # Try to union with 4 neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < M and 0 <= nc < N and visited[nr][nc]:
                        neighbor_idx = nr * N + nc
                        union(idx, neighbor_idx)
                cell_idx += 1

            # Check if (0, 0) is added to any component
            if visited[0][0]:
                result[qi] = size[find(0)]
            else:
                result[qi] = 0

        return result