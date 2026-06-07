from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        children = set()
        for parent, child, isLeft in descriptions:
            if child not in mp:
                mp[child] = TreeNode(child, None, None)
            if parent not in mp:
                mp[parent] = TreeNode(parent, None, None)

            if isLeft == 1:
                mp[parent].left = mp[child]
            else:
                mp[parent].right = mp[child]
            children.add(child)
        for node in mp:
            if node not in children:
                return mp[node]



# Time Complexity: O(n)
# Space Complexity: O(no of nodes)