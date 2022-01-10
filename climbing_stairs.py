class Solution:
    def climb_stairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        a, b, c = 0, 1, 2
        for i in range(3, n + 1):
            a, b = b, c
            c = a + c

        return c


if __name__ == '__main__':
    solution = Solution()
    print(solution.climb_stairs(3))
