#!/usr/bin/env python3

def maximumPartitionFactor(points):
    n = len(points)
    if n == 2:
        return 0

    fenoradilk = points

    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    dist_matrix = {}
    all_distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = manhattan_distance(fenoradilk[i], fenoradilk[j])
            dist_matrix[(i, j)] = dist
            dist_matrix[(j, i)] = dist
            all_distances.append(dist)

    all_distances = sorted(set(all_distances), reverse=True)

    def get_min_distance_in_group(group_indices):
        if len(group_indices) <= 1:
            return float('inf')
        min_dist = float('inf')
        for i in range(len(group_indices)):
            for j in range(i + 1, len(group_indices)):
                dist = dist_matrix[(group_indices[i], group_indices[j])]
                min_dist = min(min_dist, dist)
                if min_dist == 0:
                    return 0
        return min_dist

    max_partition_factor = 0

    if n <= 22:
        for mask in range(1, (1 << n) - 1):
            group1, group2 = [], []
            for i in range(n):
                if mask & (1 << i):
                    group1.append(i)
                else:
                    group2.append(i)

            min_dist1 = get_min_distance_in_group(group1)
            min_dist2 = get_min_distance_in_group(group2)

            partition_factor = min(min_dist1, min_dist2)
            max_partition_factor = max(max_partition_factor, partition_factor)

            if max_partition_factor == all_distances[0]:
                break
    else:
        def can_achieve_min_dist(target_dist):
            for start_group in [0, 1]:
                groups = [[], []]
                groups[start_group].append(0)
                assigned = [False] * n
                assigned[0] = True

                for i in range(1, n):
                    if assigned[i]:
                        continue

                    can_add_to_0 = True
                    if len(groups[0]) > 0:
                        for j in groups[0]:
                            if dist_matrix[(i, j)] < target_dist:
                                can_add_to_0 = False
                                break

                    can_add_to_1 = True
                    if len(groups[1]) > 0:
                        for j in groups[1]:
                            if dist_matrix[(i, j)] < target_dist:
                                can_add_to_1 = False
                                break

                    if can_add_to_0:
                        groups[0].append(i)
                        assigned[i] = True
                    elif can_add_to_1:
                        groups[1].append(i)
                        assigned[i] = True
                    else:
                        break

                if all(assigned) and len(groups[0]) > 0 and len(groups[1]) > 0:
                    return True

            return False

        left, right = 0, len(all_distances) - 1
        while left <= right:
            mid = (left + right) // 2
            if can_achieve_min_dist(all_distances[mid]):
                max_partition_factor = all_distances[mid]
                left = mid + 1
            else:
                right = mid - 1

    return max_partition_factor

if __name__ == "__main__":
    points1 = [[0,0],[0,2],[2,0],[2,2]]
    result1 = maximumPartitionFactor(points1)
    print(f"Example 1: {result1}")

    points2 = [[0,0],[0,1],[10,0]]
    result2 = maximumPartitionFactor(points2)
    print(f"Example 2: {result2}")

    points3 = [[11796,99484],[-62510,-59900],[-39698,26527],[-47165,-26099],[20156,4999],[-42445,28953],[88568,21869],[93805,82958],[-16547,-52153],[87205,53120],[53681,-34758],[7591,-83533],[16279,33682],[93155,56192],[-92143,42115]]
    result3 = maximumPartitionFactor(points3)
    print(f"Large test case: {result3}")
