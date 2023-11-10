class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        # Find the start of the array (a node with only one neighbor)
        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break
        
        
        stack = [root]  
        ans = []
        visited = set()
        visited.add(root)
        while stack:
            node = stack.pop()
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited: 
                    stack.append(neighbor)
                    visited.add(neighbor)
            graph[node] = []

        return ans