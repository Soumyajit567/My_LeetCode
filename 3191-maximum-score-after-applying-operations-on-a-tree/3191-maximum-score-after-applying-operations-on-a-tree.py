class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(edges)+1
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        def fn(u, p): 
            """Return """
            val = s = 0 
            for v in graph[u]: 
                if v != p: 
                    vv, ss = fn(v, u)
                    val += vv 
                    s += ss
            if graph[u] != [p]: val += values[u]
            return max(val, s), s+values[u]
        
        return fn(0, -1)[0]