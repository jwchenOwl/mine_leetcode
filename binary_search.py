from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        middle_suffix = nums_len // 2
        temp = middle_suffix
        while True:
            if nums[middle_suffix] > target:
                nums = nums[0:middle_suffix]
                temp = temp - len(nums)
                middle_suffix = len(nums) // 2

            elif nums[middle_suffix] < target:
                nums = nums[middle_suffix:]
                temp = temp + len(nums) // 2
                middle_suffix = len(nums) // 2
            elif nums[middle_suffix] == target:
                return temp
            print(nums,middle_suffix,temp)
            if len(nums) == 1:
                if nums[0] == target:
                    return temp if temp > 0 else 0
                else:
                    return -1
            if len(nums) ==0:
                return -1

if __name__ == '__main__':
    s = Solution()
    a = s.search(
        [-1,0,3,5,9,12], 0)
    print(a)
