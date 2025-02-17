# Problem: Akash and Dinner (https://www.codechef.com/problems/CHEFDINE)
# Approach: Use a dictionary to store the minimum time for each category
# Time Complexity: O(n), Space Complexity: O(n)

t = int(input())
for _ in range(t):  
    n,k = map(int,input().split())  
    cat = list(map(int,input().split()))  
    time = list(map(int,input().split()))  
    d = {}  

    for i in range(len(cat)):  
        if cat[i] not in d:   
            d[cat[i]] = time[i]  
        else:   
            d[cat[i]] = min(d[cat[i]], time[i])  

    if len(d) < k:  
        print(-1)  
    else:  
        my_list = d.values()  
        smallest = sorted(my_list)[:k]  
        print(sum(smallest))  