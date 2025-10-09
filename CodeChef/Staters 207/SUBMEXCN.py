import sys
MOD = 998244353

def precompute_fact(limit):
    fact = [1]*(limit+1)
    invfact = [1]*(limit+1)
    for i in range(1, limit+1):
        fact[i] = fact[i-1]*i % MOD
    invfact[limit] = pow(fact[limit], MOD-2, MOD)
    for i in range(limit, 0, -1):
        invfact[i-1] = invfact[i]*i % MOD
    return fact, invfact

def comb(n,k,fact,invfact):
    if k < 0 or k > n or n < 0:
        return 0
    return fact[n]*invfact[k]%MOD*invfact[n-k]%MOD

def solve():
    it = iter(sys.stdin.buffer.read().split())
    t = int(next(it))
    Ns = []
    maxN = 0
    for _ in range(t):
        n = int(next(it))
        Ns.append(n)
        if n > maxN: maxN = n
    # Need factorials up to 2*maxN
    fact, invfact = precompute_fact(2*maxN+5)
    out_lines = []
    for N in Ns:
        if N == 1:
            # Only arrays: [0]; outputs for M=1: f sum over arrays -> for array [0], subsequences length1: mex values {1} size1
            out_lines.append('1')
            continue
        A0 = comb(2*N -1, N -1, fact, invfact)
        # Precompute B_x prefix for x=1..N-1
        prefix_B = [0]*(N)
        for x in range(1, N):
            Bx = comb(2*N - x -1, N -1, fact, invfact)
            prefix_B[x] = (prefix_B[x-1] + Bx) % MOD
        # Precompute P[k] = sum_{i=0..k} C(i, N-1)
        # Need k up to 2N -3
        P = [0]*(2*N)
        for k in range(N-1, 2*N -2):  # last needed index 2N-3 inclusive
            P[k] = (P[k-1] + comb(k, N -1, fact, invfact)) % MOD
        base_idx = N -2  # P[N-2]
        base_val = P[base_idx] if base_idx >=0 else 0
        ans = []
        for M in range(1, N+1):
            term1 = (A0 - comb(N + M -2, N -1, fact, invfact)) % MOD
            term2 = prefix_B[M-1]  # sum x=1..M-1
            # But we need sum_{x=1..M} B_x; add B_M if M<=N-1
            if M <= N-1:
                term2 = (term2 + comb(2*N - M -1, N -1, fact, invfact)) % MOD
            # term3: sum_{x=1..M-1} C(N + M - x -2, N -1) = sum_{y=N-1..N+M-3} C(y, N-1)
            if M >= 2:
                high = N + M -3
                term3 = (P[high] - base_val) % MOD
            else:
                term3 = 0
            val = (term1 + term2 - term3) % MOD
            if M == N:
                val = (val + 1) % MOD
            ans.append(str(val))
        out_lines.append(' '.join(ans))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == '__main__':
    solve()

