# We visit everything on the left side of a node, print the node, and then visit everything on the right side of the node

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack,result = [],[]
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return result
