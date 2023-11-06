class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [(0, -1, True)]
        results = {i: (0, 0) for i in range(n)}
        visited = set()
        new_set = set()
        new_set.add(0)

        while stack:
            node, parent, is_first_time = stack.pop()

            if node in visited:
                continue

            if is_first_time:
                stack.append((node, parent, False))  
                for child in graph[node]:
                        if child not in new_set:
                            stack.append((child, node, True)) 
                            new_set.add(child) 
            else:
                visited.add(node)
                val = values[node] if graph[node] != [parent] else 0
                s = 0
                for child in graph[node]:
                    if child != parent:
                        val += results[child][0]
                        s += results[child][1]
                results[node] = (max(val, s), s + values[node])
        print(results)


        return results[0][0]

"""
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        def prune(cur):
            for poss in graph[cur]:
                graph[poss].remove(cur)
                prune(poss)
        prune(0)
        
        
        @cache
        def calc(node, there_is_up):
            if there_is_up:
                score = values[node]
                for poss in graph[node]:
                    score += calc(poss, True)
                return score
            else:
                if len(graph[node]) == 0:
                    return 0
                else:
                    a = values[node]
                    b = 0
                    for poss in graph[node]:
                        a += calc(poss, False)
                        b += calc(poss, True)
                    return max(a, b)
                
        return calc(0, False)



"""