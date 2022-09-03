class Solution:
    def preorder(self, root:'Node')->List[int]:
        """
        Solution 1 using Recursive
        """
        output = []

        def dfs(node):
            if not node:
                return
            output.append(node.val)

            for c in node.children:
                dfs(c)
        dfs(root)
        return output

        """
        Solution 2 using Iterating
        """
        if not root:
            return[]
        q = deque([root])
        output = []

        while q:
            cand = q.popleft()
            output.append(cand.val)

            for c in reversed(cand.children):
                q.appendleft(c)
        return output
