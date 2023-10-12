class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i : [] for i in range(1, n + 1)}
        count = {i : 0 for  i in range(1, n + 1)}
        for start, end in relations:
            graph[start].append(end)
            count[end] += 1
        queue = deque([])
        for node in graph:
            if count[node] == 0:
                queue.append(node)

        
        step = 0
        studied_count = 0
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                node = queue.popleft()
                studied_count += 1
                for neighbor in graph[node]:
                    count[neighbor] -= 1
                    if count[neighbor] == 0:
                        queue.append(neighbor)
        return step if studied_count == n else -1

