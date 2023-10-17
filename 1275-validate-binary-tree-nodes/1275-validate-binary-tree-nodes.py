class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = defaultdict(int)
        
        for i in range(n): 
            if leftChild[i] != -1: 
                indegree[leftChild[i]] += 1 
            if rightChild[i] != -1: 
                indegree[rightChild[i]] += 1 
        
        for i in range(n): 
            if indegree[i] > 1: return False 
        
        q = deque([i for i in range(n) if not indegree[i]]) 
        visited = set(q) 
        if len(q) > 1: return False 
        while q: 
            curr = q.popleft() 
            if leftChild[curr] != -1: 
                indegree[leftChild[curr]] -= 1 
                if not indegree[leftChild[curr]]: 
                    visited.add(leftChild[curr])
                    q.append(leftChild[curr])
            if rightChild[curr] != -1: 
                indegree[rightChild[curr]] -= 1 
                if not indegree[rightChild[curr]]: 
                    visited.add(rightChild[curr])
                    q.append(rightChild[curr])

        return len(visited) == n 