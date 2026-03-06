class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        for ind, i in enumerate(s):
            if i == ']':
                temp = ''
                while st[-1] != '[':
                    temp = st.pop() + temp
                st.pop()
                num = ''
                while st and st[-1].isdigit():
                    num = st.pop() + num
                st.append(temp * int(num))
            else:
                st.append(i)

        return ''.join(st)