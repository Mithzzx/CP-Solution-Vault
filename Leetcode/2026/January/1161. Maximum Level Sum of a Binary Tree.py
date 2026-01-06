#Problem link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
#Time Complexity: O(n), Space Complexity: O(n)
#Approach: Use a queue to traverse the tree level-wise and keep track of the maximum sum at each level
#Data Structure: Queue, Tree, Algorithm: BFS


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        idx, Sum=0, -inf
        q=deque()
        q.append(root)
        level=1
        while q:
            qz=len(q)
            curSum=0
            for i in range(qz):
                Node=q.popleft()
                curSum+=Node.val
                if Node.left: q.append(Node.left)
                if Node.right: q.append(Node.right)
            if curSum>Sum:
                idx, Sum=level, curSum
            level+=1
        return idx