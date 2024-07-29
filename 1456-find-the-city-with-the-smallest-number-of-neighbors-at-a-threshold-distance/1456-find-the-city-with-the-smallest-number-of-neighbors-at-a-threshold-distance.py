import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(start):
            distances = [float('inf')] * n
            distances[start] = 0
            heap = [(0, start)]
            
            while heap:
                current_dist, node = heapq.heappop(heap)
                if current_dist > distances[node]:
                    continue
                for neighbor, weight in graph[node]:
                    distance = current_dist + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(heap, (distance, neighbor))
            return distances
        

        min_city_count = float('inf')
        result_city = -1
        
        for i in range(n):
            distances = dijkstra(i)
            reachable_cities_count = sum(1 for d in distances if d <= distanceThreshold)
            
            if (reachable_cities_count < min_city_count or reachable_cities_count == min_city_count) and i > result_city:
                min_city_count = reachable_cities_count
                result_city = i
        
        return result_city



# class Solution:
#     def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
#         dist = [[float('inf')] * n for _ in range(n)]
#         for i in range(n):
#             dist[i][i] = 0
#         for u, v, w in edges:
#             dist[u][v] = w
#             dist[v][u] = w
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     if dist[i][j] > dist[i][k] + dist[k][j]:
#                         dist[i][j] = dist[i][k] + dist[k][j]
#         min_city_count = float('inf')
#         result_city = -1
#         for i in range(n):
#             count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
#             if count <= min_city_count:
#                 min_city_count = count
#                 result_city = i
        
#         return result_city