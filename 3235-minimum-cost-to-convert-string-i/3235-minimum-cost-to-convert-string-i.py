class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
            INF = float('inf')
            ALPHABET = string.ascii_lowercase
            graph = {ch: {ch2: INF for ch2 in ALPHABET} for ch in ALPHABET}
            for ch in ALPHABET:
                graph[ch][ch] = 0  
            for o, c, co in zip(original, changed, cost):
                graph[o][c] = min(graph[o][c], co)  
            for k in ALPHABET:
                for i in ALPHABET:
                    for j in ALPHABET:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

            total_cost = 0
            for s_char, t_char in zip(source, target):
                if graph[s_char][t_char] == INF:
                    return -1  
                total_cost += graph[s_char][t_char]

            return total_cost