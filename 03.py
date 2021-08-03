class Solution(object):
    def indexToSubset(self, nums, index):
        subset = []
        for i in range(len(nums)):
            reverse_index = len(nums)-1-i
            new_factor = 2**reverse_index
            if not index: break
            if index > new_factor: 
                index -= new_factor
                subset.append(nums[i])
        return list(sorted(subset)) 
                
    def subsetsWithDup(self, nums):
        subset_list = {}
        for i in range(2**len(nums)):
            new_subset = self.indexToSubset(nums, i)
            subset_list.update({str(new_subset): new_subset})
        subset_list.update({str(nums): nums})
        return list(subset_list.values())