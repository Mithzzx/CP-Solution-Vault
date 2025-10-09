import sys

def distance(ax, ay, x, y):
    return abs(x - ax) + abs(y - ay)

it = iter(sys.stdin.buffer.read().strip().split())
try:
    t = int(next(it))
except StopIteration:
    t = 0
out_lines = []
for _ in range(t):
    # Correct order: N A B
    n = int(next(it)); A = int(next(it)); B = int(next(it))
    # Initialize answer with a large value
    best = None
    for _ in range(n):
        x = int(next(it)); y = int(next(it))
        d = distance(A, B, x, y)
        if best is None or d < best:
            best = d
    # best must be set because n >= 1 per problem statement
    out_lines.append(str(best if best is not None else 0))

sys.stdout.write("\n".join(out_lines))
