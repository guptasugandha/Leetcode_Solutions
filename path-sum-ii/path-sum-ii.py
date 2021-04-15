# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def dfs(node, pathList, target):
            if not node:
                return
            target = target-node.val
            
            if (not node.left) and (not node.right) and target == 0:
                pathList.append( node.val )
                answer.append( pathList )
                return
            
            dfs(node.left, pathList + [node.val], target)
            dfs(node.right, pathList + [node.val], target)
            return
        
        answer = []
        dfs(node=root, pathList=[], target=targetSum)
        return answer