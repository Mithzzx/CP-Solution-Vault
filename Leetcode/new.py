def countPromotionalPeriods(orders):
    n = len(orders)
    if n < 3:
        return 0

    next_greater = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and orders[stack[-1]] < orders[i]:
            stack.pop()
        if stack:
            next_greater[i] = stack[-1]
        else:
            next_greater[i] = n
        stack.append(i)

    prev_greater = [-1] * n
    stack = []
    for i in range(n):
        while stack and orders[stack[-1]] < orders[i]:
            stack.pop()
        if stack:
            prev_greater[i] = stack[-1]
        else:
            prev_greater[i] = -1
        stack.append(i)

    events1 = []
    for i in range(n):
        events1.append((next_greater[i], i))
    events1.sort(key=lambda x: x[0], reverse=True)

    def fenw_add(fenw, index, size_n, delta):
        idx = index + 1
        while idx <= size_n:
            fenw[idx] += delta
            idx += idx & -idx

    def fenw_prefix(fenw, index, size_n):
        if index < 0:
            return 0
        total = 0
        idx = index + 1
        while idx > 0:
            total += fenw[idx]
            idx -= idx & -idx
        return total

    def fenw_range_query(fenw, l, r, size_n):
        if l > r:
            return 0
        return fenw_prefix(fenw, r, size_n) - fenw_prefix(fenw, l - 1, size_n)

    size_fen = n
    fenw1 = [0] * (size_fen + 1)
    left_count = 0
    ptr1 = 0
    for j in range(n - 1, -1, -1):
        while ptr1 < len(events1) and events1[ptr1][0] > j:
            i_val = events1[ptr1][1]
            fenw_add(fenw1, i_val, size_fen, 1)
            ptr1 += 1
        if j < 2:
            continue
        low_bound = prev_greater[j]
        if low_bound == -1:
            low_bound = 0
        else:
            low_bound = prev_greater[j]
        high_bound = j - 2
        if low_bound > high_bound:
            cnt = 0
        else:
            cnt = fenw_range_query(fenw1, low_bound, high_bound, size_fen)
        left_count += cnt

    events2 = []
    for i in range(n):
        events2.append((next_greater[i], i))
    events2.sort(key=lambda x: x[0], reverse=True)

    fenw2 = [0] * (size_fen + 1)
    ptr2 = 0
    right_count = 0
    for j in range(n - 1, -1, -1):
        while ptr2 < len(events2) and events2[ptr2][0] >= j:
            i_val = events2[ptr2][1]
            fenw_add(fenw2, i_val, size_fen, 1)
            ptr2 += 1
        if j < 2:
            continue
        low_bound = prev_greater[j] + 1
        high_bound = j - 2
        if low_bound > high_bound:
            cnt = 0
        else:
            cnt = fenw_range_query(fenw2, low_bound, high_bound, size_fen)
        right_count += cnt

    return left_count + right_count

print(countPromotionalPeriods([4, 3, 5, 5, 3]))