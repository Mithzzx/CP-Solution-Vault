# Problem: https://www.codechef.com/START181D/problems/FINDOUT
# Approach: Find two elements in the array such that their sum is not present in the array
# Time Complexity: O(n^2), Space Complexity: O(n)

def find_outside_array(arr):
    n = len(arr)
    arr_set = set(arr)

    if n == 1 or len(arr_set) == 1:
        element = arr[0]
        if element + element not in arr_set:
            return element, element
        return -1

    max_val = max(arr)
    if max_val + max_val not in arr_set:
        return max_val, max_val

    min_val = min(arr)
    if min_val + min_val not in arr_set:
        return min_val, min_val

    if min_val + max_val not in arr_set:
        return min_val, max_val

    for num in arr_set:
        if num + num not in arr_set:
            return num, num

    check_arr = list(arr_set)
    if len(check_arr) > 1000:
        check_arr = check_arr[:1000]

    for i in range(len(check_arr)):
        for j in range(i + 1, len(check_arr)):
            sum_val = check_arr[i] + check_arr[j]
            if sum_val not in arr_set:
                return check_arr[i], check_arr[j]

    sorted_arr = sorted(arr_set)
    step = max(1, len(sorted_arr) // 100)
    selected = sorted_arr[::step]

    for i in range(len(selected)):
        for j in range(len(selected)):
            sum_val = selected[i] + selected[j]
            if sum_val not in arr_set:
                return selected[i], selected[j]

    first = arr[0]
    for num in arr_set:
        if first != num:
            if first + num not in arr_set:
                return first, num

    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    result = find_outside_array(arr)
    if result == -1:
        print(-1)
    else:
        print(result[0], result[1])
