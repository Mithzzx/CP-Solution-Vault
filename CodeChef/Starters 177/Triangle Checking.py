# Problem : Starters177D Triangle Checking
# Link: http://codechef.com/START177D/problems/TRICHECK
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: Check if the sum of any two sides is greater than the third side

a,b,c = map(int,input().split())
print("Yes" if a + b > c and b + c > a and a + c > b else "No" )