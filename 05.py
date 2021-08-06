class Solution(object):
    def __init__(self):
        self.dictionary = {}
    def stoneGameRecursive(self, piles, i, j):
        if i > j: return 0
        fromFirst = hash(str(i+1)+"-"+str(j))
        fromLast = hash(str(i)+"-"+str(j-1))
        try:
            firstResult = self.dictionary[fromFirst]
        except:
            firstResult = self.stoneGameRecursive(piles, i+1, j)
            self.dictionary.update({fromFirst: firstResult})
        try:
            lastResult = self.dictionary[fromLast]
        except:
            lastResult = self.stoneGameRecursive(piles, i, j-1)
            self.dictionary.update({fromLast: lastResult})
        return max(piles[i]+firstResult, piles[j]+lastResult)
    def stoneGame(self, piles):
        return 2 * self.stoneGameRecursive(piles, 0, len(piles)-1) > sum(piles)
if __name__=="__main__":
    solution = Solution()
    piles = [7,7,12,16,41,48,41,48,11,9,34,2,44,30,27,12,11,39,31,8,23,11,47,25,15,23,4,17,11,50,16,50,38,34,48,27,16,24,22,48,50,10,26,27,9,43,13,42,46,24]
    print(solution.stoneGame(piles))