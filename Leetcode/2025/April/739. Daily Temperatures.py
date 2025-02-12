#Problem: https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium
# Approach: Use a stack to keep track of indices of temperatures
# Time Complexity: O(n), Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures):
        st = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                res[idx] = i - idx
            st.append(i)

        return res
