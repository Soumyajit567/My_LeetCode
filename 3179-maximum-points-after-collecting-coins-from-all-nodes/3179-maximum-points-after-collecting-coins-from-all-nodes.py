class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            
        second_way_points = [0]*n
        def calc_2_way(node, parent):
            pts = [coins[node]//2]
            for child in g[node]:
                if parent != child:
                    pts += [x//2 for x in calc_2_way(child, node) if x >= 2]
            second_way_points[node] = sum(pts)
            return pts
            
        def dfs(node, parent):
            points = coins[node]-k
            for child in g[node]:
                if parent != child:
                    points += dfs(child, node)
            return max(points, second_way_points[node])
        
        calc_2_way(0, -1)
        return dfs(0, -1)
            