from collections import deque

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, N + 1)}
        in_count = {i: 0 for i in range(1, N + 1)}  # or in-degree
        for start_node, end_node in relations:
            graph[start_node].append(end_node)
            in_count[end_node] += 1

        queue = deque()
        for node in graph:
            if in_count[node] == 0:
                queue.append(node)

        step = 0
        studied_count = 0
        # start learning with BFS
        while queue:
            # start new semester
            step += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                studied_count += 1
                end_nodes = graph[node]
                for end_node in end_nodes:
                    in_count[end_node] -= 1
                    # if all prerequisite courses learned
                    if in_count[end_node] == 0:
                        queue.append(end_node)

        return step if studied_count == N else -1
