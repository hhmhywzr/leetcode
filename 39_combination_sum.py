class Solution(object):
    # def combinationSum(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type tatget: int
    #     :rtype List[List[int]]
    #     """
    #     nums = []
    #     indexes = []
    #     returnLists = []
    #     sum = 0
    #     i = 0
    #     candidates.sort()
    #     while True:
    #         while i >= len(candidates):
    #             if len(nums) == 0:
    #                 return returnLists
    #             sum -= nums.pop()
    #             i = indexes.pop()+1
    #         if sum + candidates[i] < target:
    #             nums.append(candidates[i])
    #             indexes.append(i)
    #             sum += candidates[i]
    #         elif sum + candidates[i] > target:
    #             if len(nums) > 0:
    #                 sum -= nums.pop()
    #                 i = indexes.pop()+1
    #             else:
    #                 return returnLists
    #         elif sum + candidates[i] == target:
    #             newNums = nums[:]
    #             newNums.append(candidates[i])
    #             returnLists.append(newNums)
    #             if len(nums) > 0:
    #                 sum -= nums.pop()
    #                 i = indexes.pop()+1
    #             else:
    #                 i += 1

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type tatget: int
        :rtype List[List[int]]
        """
        solutions = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], solutions)
        return solutions

    def dfs(self, nums, start_index, target, solution, solutions):
        i = start_index
        while i < len(nums):
            num = nums[i]
            if num == target:
                solution.append(num)
                solutions.append(solution)
                return
            elif num < target:
                solution.append(num)
                self.dfs(nums, i, target-num, solution[:], solutions)
                solution.pop()
            else:
                return
            i += 1


assert Solution().combinationSum([2, 3, 4], 7) == [[2, 2, 3], [3, 4]]
assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
assert Solution().combinationSum([2], 1) == []
