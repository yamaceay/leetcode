class Solution(object):
    def __init__(self):
        self.dic = {}
    def isPalindrome(self, s):
        if len(s) > 1:
            fromFirst = len(s)//2
            return all([s[i] == s[-i-1] for i in range(fromFirst)])
        return True
    def minCutHelper(self, s, i, j):
        unique = str(i)+"-"+str(j)
        try:
            isValid = self.dic[unique]
        except:
            isValid = self.isPalindrome(s[i:j])
            self.dic.update({unique: isValid})
        if isValid:
            return 0
        minimum = len(s)
        for k in range(i+1, j):
            fromLeft = self.minCutHelper(s, i, k)
            fromRight = self.minCutHelper(s, k, j)
            minimum = min(fromLeft + 1 + fromRight, minimum)
        return minimum
    def minCut(self, s):
        return self.minCutHelper(s, 0, len(s))