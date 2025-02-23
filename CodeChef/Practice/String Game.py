# URL: https://www.codechef.com/problems/STRAME
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Use a stack to store the characters of the string and pop the top element if it is equal to the current element
# Data Structure: Stack

s = ['1', '0', '1']
x = 0
st =[]

while True:
    for i in range(len(s)):
        if st:
            if s[i] != st[-1]:
                st.pop()
                x+=1
                continue
        st.append(s[i])
    if len(st) == len(s): break
    st,s = [],st

print(x)

