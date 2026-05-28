from typing import List

# Approach 1
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class Node:
            def __init__(self):
                self.index = -1
                self.child = {}
        
        def printNode(node, s):
            if node:
                for k in node.child:
                    print(s+"- "+k)
                    printNode(node.child[k], s+"   ")
                
        
        n = len(wordsContainer)
        pairs = [(wordsContainer[i], i) for i in range(n)]
        pairs.sort(key = lambda x: len(x[0]))
        
        root = Node()
        root.index = pairs[0][1]
        for word, idx in pairs:
            word = word[::-1]
            curr = root
            for ch in word: 
                if ch not in curr.child:
                    curr.child[ch] = Node()
                    curr.child[ch].index = idx
                curr = curr.child[ch]

        ans = []
        for word in wordsQuery:
            curr = root
            word = word[::-1]
            for ch in word:
                if ch not in curr.child:
                    break
                curr = curr.child[ch]
            ans.append(curr.index)
            
        return ans


# Time Complexity: O(n*log(n) + T_wc + T_qc), where:
# - n is the number of words in wordsContainer, 
# - T_wc is the time complextiy for creating the trie, which is the total number of characters in wordsContainer
# - T_qc is the time complexity for processing the queries, which is the total number of characters in wordsQuery.

# Space Complexity: O(T_wc), where T_wc is the total number of characters in wordsContainer, which is the space used by the trie.