import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    ptr = 1
    out_lines = []
    for _ in range(t):
        n = int(data[ptr]); k = int(data[ptr+1]); ptr += 2
        s = data[ptr]; ptr += 1
        if n == k:
            out_lines.append('-' * n)
            continue
        count0 = s.count('0')
        count1 = s.count('1')
        count2 = k - count0 - count1
        Tmin = count0
        Tmax = count0 + count2
        Bmin = count1
        Bmax = count1 + count2
        # Build result
        res = []
        left_removal_limit = Tmin  # indices 1..Tmin always removed
        right_removal_start = n - Bmin + 1  # indices from here to n always removed
        always_keep_left = Tmax + 1
        always_keep_right = n - Bmax  # inclusive
        for i in range(1, n + 1):
            if i <= left_removal_limit or i >= right_removal_start:
                res.append('-')
            elif always_keep_left <= i <= always_keep_right:
                res.append('+')
            else:
                res.append('?')
        out_lines.append(''.join(res))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == '__main__':
    solve()

