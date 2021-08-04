from copy import deepcopy as cpy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSumRecursive(self, tmp, targetSum, path):
        results = []
        if tmp:
            path.append(tmp.val)
            if sum(path) == targetSum and not tmp.left and not tmp.right: results.append(path)
            else:
                leftPath = cpy(path)
                rightPath = cpy(path)
                leftRes = self.pathSumRecursive(tmp.left, targetSum, leftPath)
                rightRes = self.pathSumRecursive(tmp.right, targetSum, rightPath)
                if leftRes:
                    results.extend(leftRes)
                if rightRes:
                    results.extend(rightRes)
        return results
        
    def pathSum(self, root, targetSum):
        tmp = cpy(root)
        paths = self.pathSumRecursive(tmp, targetSum, [])
        return paths