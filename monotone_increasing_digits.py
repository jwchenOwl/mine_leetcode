class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = list([int(i) for i in str(n)])
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i - 1] = nums[i - 1] - 1
                nums[i:] = list([int(i) for i in len(nums[i:]) * '9'])
        a = 0
        for index, i in enumerate(nums):
            a += i * (10 ** (len(nums) - index))
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.monotoneIncreasingDigits(332123151326218589732654789124368713245897231412351234325))
