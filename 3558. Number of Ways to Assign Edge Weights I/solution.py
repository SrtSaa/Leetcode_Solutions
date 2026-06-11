from typing import List

class Solution:
    def dfs(self, adj, x, par, depth):
        maxDepth = depth
        for v in adj[x]:
            if v!=par:
                maxDepth = max(maxDepth, self.dfs(adj, v, x, depth+1))
        return maxDepth
    
    def pow(self, x, y):
        MOD = 10**9+7
        res = 1
        base = x
        while(y):
            if y&1:
                res = res * base % MOD
            base = (base * base) % MOD
            y >>= 1
        return res
    
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        nodes = len(edges) + 1
        adj = {}
        for u, v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)
        
        mx = self.dfs(adj, 1, 0, 0)
        return self.pow(2, mx-1)
        


# Time Complexity: O(N) where N is the number of nodes in the tree, since we need to traverse all the nodes to find the maximum depth of the tree. The power function runs in O(log y) time, where y is the maximum depth of the tree, which is at most O(N) in the worst case. Therefore, the overall time complexity is O(N).
# Space Complexity: O(N) where N is the number of nodes in the tree, since we need to store the adjacency list of the tree and the recursive call stack for the depth-first search. The maximum depth of the tree can be O(N) in the worst case, which contributes to the space complexity.