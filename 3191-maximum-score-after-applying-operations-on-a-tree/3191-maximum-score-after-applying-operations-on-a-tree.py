class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # State: (node, parent, is_first_time)
        stack = [(0, -1, True)]
        # Stores tuple (val, s) for each node
        results = {i: (0, 0) for i in range(n)}
        # Track visited to not reprocess nodes
        visited = set()

        while stack:
            node, parent, is_first_time = stack.pop()

            if node in visited:
                continue

            if is_first_time:
                # If it's the first time visiting this node, 
                # we need to process all children before this node
                stack.append((node, parent, False))  # Add node back to stack to process after children
                for child in graph[node]:
                    if child != parent:
                        stack.append((child, node, True))  # Process children
            else:
                # Process node after all children have been processed
                visited.add(node)
                val = values[node] if graph[node] != [parent] else 0
                s = 0
                for child in graph[node]:
                    if child != parent:
                        val += results[child][0]
                        s += results[child][1]
                # Save the results
                results[node] = (max(val, s), s + values[node])

        # The result for the root node will be in results[0]
        return results[0][0]

