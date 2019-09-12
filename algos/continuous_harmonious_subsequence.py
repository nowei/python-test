class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        c_i = 1
        i = 1
        m_length = 1
        h_max = 0
        h_min = 0
        while i < len(nums):
            if abs(nums[i - 1] - nums[i]) == 1:
                h_max = max(nums[i - 1], nums[i])
                h_min = min(nums[i - 1], nums[i])
                while i < len(nums) and nums[i] == h_max or nums[i] == h_min:
                    i += 1
                    c_i += 1
                if c_i > m_length:
                    m_length = c_i
                c_i = 0
            else:
                i += 1
        return m_length