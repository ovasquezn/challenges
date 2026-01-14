"""
Problem: 865. Smallest Subtree with all the Deepest Nodes (LeetCode)

Data Structure:
Binary Tree
- Each node has: val, left, right
- Unique node values
- 1 ≤ number of nodes ≤ 500

Definitions:
- Depth of a node = distance from the root.
- Deepest nodes = nodes with the maximum depth in the entire tree.
- Subtree of a node = that node + all its descendants.

Task:
Return the root of the smallest subtree that contains ALL the deepest nodes.

Key Insight:
The smallest subtree that contains all deepest nodes is rooted at
the Lowest Common Ancestor (LCA) of all deepest nodes.

Example:
Input:
root = [3,5,1,6,2,0,8,null,null,7,4]

Deepest nodes:
7 and 4 (maximum depth)

Valid subtrees containing them:
- rooted at 5
- rooted at 3
- rooted at 2

Smallest one:
rooted at 2

Output:
[2,7,4]

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0, None

            hl, cl = dfs(node.left)
            hr, cr = dfs(node.right)

            if hl == hr:
                return hl + 1, node
            elif hl > hr:
                return hl + 1, cl
            else:
                return hr + 1, cr

        return dfs(root)[1]

from collections import deque

def build_tree(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root


def print_tree(root):
    """Level-order print (LeetCode style)"""
    if not root:
        print([])
        return

    res = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)

    while res and res[-1] is None:
        res.pop()

    print(res)


root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
ans = Solution().subtreeWithAllDeepest(root)
print_tree(ans)