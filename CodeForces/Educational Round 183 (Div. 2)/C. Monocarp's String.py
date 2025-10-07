# Solution for Codeforces problem "Monocarp's String".
# Goal: remove minimal length consecutive substring so remaining counts of 'a' and 'b' equal.
# Let total difference D = total_a - total_b.
# Need substring with (a_sub - b_sub) = D so that after removal totals equal.
# Find minimal length substring with prefix[r]-prefix[l] = D.
# If D == 0 answer 0 (remove nothing). If minimal found length == n (only whole string) output -1.
# Otherwise output that minimal length.
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    try:
        t = int(next(it))
    except StopIteration:
        return
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        s = next(it)
        # total difference
        total_a = s.count('a')
        total_b = n - total_a
        D = total_a - total_b
        if D == 0:
            out_lines.append('0')
            continue
        # Prefix difference array not stored fully; keep running value and earliest index for each diff.
        earliest = {0: 0}
        pref = 0
        best = n + 1  # sentinel larger than n
        for i, ch in enumerate(s, 1):  # 1-based prefix index
            pref += 1 if ch == 'a' else -1
            target = pref - D
            if target in earliest:
                length = i - earliest[target]
                if length < best:
                    best = length
            # record earliest occurrence only
            if pref not in earliest:
                earliest[pref] = i
        if best <= n - 1:
            out_lines.append(str(best))
        else:
            out_lines.append('-1')
    sys.stdout.write('\n'.join(out_lines))

if __name__ == '__main__':
    solve()

