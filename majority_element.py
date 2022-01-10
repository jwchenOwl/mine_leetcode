from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        kw = {}
        if len(nums) ==1 :
            return nums[0]
        middle_len = len(nums) / 2
        for num in nums:
            if num not in kw:
                kw[num] = [num]
            else:
                kw[num].append(num)
                if len(kw[num]) > middle_len:
                    return num

    def more_majority_element(self, nums:List[int]) ->int:
        major = None
        count = 0
        for num in nums:
            if count == 0:
                major = num
                count += 1
                continue
            if major == num:
                count += 1
                continue
            else:
                count -= 1
        return major


if __name__ == '__main__':
    s = Solution()
    ret = s.more_majority_element([6,5,5])
    print(ret)
