from typing import List
import copy


class Solution:
    def rotate(self, nums: List[int], k: int):
        nums_len = len(nums)
        self._rotate(nums, 0, nums_len)
        self._rotate(nums, 0, k)
        self._rotate(nums, k, nums_len)

        return nums

    def _rotate(self, nums, start, end):
        for index in range((end - start) // 2 ):
            print(f"index {index}, start {start} end {end}")
            a = nums[index + start]
            b = nums[end - 1 - index]
            nums[index + start] = b
            nums[end - 1 - index] = a
        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
