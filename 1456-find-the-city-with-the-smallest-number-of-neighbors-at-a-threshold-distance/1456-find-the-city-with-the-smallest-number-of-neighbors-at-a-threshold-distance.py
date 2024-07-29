class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w, in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(i):
            dist = [float("inf")] * n
            dist[i] = 0
            minHeap = [(0, i)]
            while minHeap:
                curr_weight, node = heapq.heappop(minHeap)
                if curr_weight > dist[node]:
                    continue
                for neighbor, weight in graph[node]:
                    new_weight = curr_weight + weight
                    if new_weight < dist[neighbor]:
                        dist[neighbor] = new_weight
                        heapq.heappush(minHeap, (new_weight, neighbor))
            return dist

        ans = -1
        inf = 10e9
        min_count = inf
        for i in range(n):
            distances = dijkstra(i)
            cities = 0
            for d in distances:
                if d <= distanceThreshold:
                    cities += 1
            if cities <= min_count and i > ans:
                min_count = cities
                ans = i
        return ans
