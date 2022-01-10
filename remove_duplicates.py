from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]):
        """
        双指针法
        :param nums:
        :return:
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left +=1
                nums[left] = nums[right]
            right += 1

        return left + 1


if __name__ == '__main__':
    so = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print( so.removeDuplicates(nums))
    print(nums)
