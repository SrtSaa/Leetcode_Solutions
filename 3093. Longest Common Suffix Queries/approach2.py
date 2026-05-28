from typing import List

# Aprroach 2
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
                
        min_len = float('inf')
        min_len_idx = None
        
        root = Node()
        for idx, word in enumerate(wordsContainer):
            size = len(word)
            if size < min_len:
                min_len = size
                min_len_idx = idx
            word = word[::-1]
            curr = root
            for ch in word: 
                if ch not in curr.child:
                    curr.child[ch] = Node()
                    curr.child[ch].index = idx
                else:
                    if len(wordsContainer[curr.child[ch].index]) > size:
                        curr.child[ch].index = idx
                curr = curr.child[ch]
        root.index = min_len_idx

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

        
# Time Complexity: O(T_wc + T_qc), where:
# - T_wc is the time complextiy for creating the trie, which is the total number of characters in wordsContainer
# - T_qc is the time complexity for processing the queries, which is the total number of characters in wordsQuery.

# Space Complexity: O(T_wc), where T_wc is the total number of characters in wordsContainer, which is the space used by the trie.