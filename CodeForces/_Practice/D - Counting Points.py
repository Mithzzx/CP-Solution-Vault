def count_points_in_circles(n, centers, radii):
    max_radius = max(radii)
    total_points = 0

    for y in range(-max_radius, max_radius + 1):
        segments = []
        for i in range(n):
            center_x = centers[i]
            radius = radii[i]

            if abs(y) <= radius:
                dx = int((radius ** 2 - y ** 2) ** 0.5)
                segments.append((center_x - dx, center_x + dx))

        if not segments:
            continue

        segments.sort()

        merged = [segments[0]]
        for start, end in segments[1:]:
            if start <= merged[-1][1] + 1:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))

        for start, end in merged:
            total_points += end - start + 1

    return total_points

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    centers = list(map(int, input().split()))
    radii = list(map(int, input().split()))

    print(count_points_in_circles(n, centers, radii))
