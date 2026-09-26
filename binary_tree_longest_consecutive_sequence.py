class Solution:
    def longestConsecutive(self, root):
        if not root:
            return 0

        def dfs(node, parent, length):
            if not node:
                return length

            if parent and node.val == parent.val + 1:
                length += 1
            else:
                length = 1

            left = dfs(node.left, node, length)
            right = dfs(node.right, node, length)

            return max(length, left, right)

        return dfs(root, None, 0)
