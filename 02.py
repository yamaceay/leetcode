class Solution(object):
    def twoSum(self, nums, target):
        new_nums = [abs(x-float(target)/2) for x in nums]
        new_dict = {}
        for i, num in enumerate(new_nums):
            try:
                return [new_dict[str(num)], i]
            except:
                new_dict.update({str(num): i})