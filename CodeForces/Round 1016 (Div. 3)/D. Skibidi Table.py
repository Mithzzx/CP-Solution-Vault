def find_cell_value(n, x, y):
    """Find the value at cell (x, y) in a 2^n × 2^n table."""
    return get_position(n, x, y, 1, 1, 1 << n)


def find_value_position(n, d):
    """Find the position (x, y) of value d in a 2^n × 2^n table."""
    size = 1 << n  # 2^n
    return get_coordinates(n, d, 1, 1, size)


def get_position(n, x, y, start_x, start_y, size):
    """Recursive function to find the value at position (x, y)."""
    if size == 2:
        # Base case: 2×2 table
        if x == start_x and y == start_y:  # top-left
            return 1
        elif x == start_x + 1 and y == start_y + 1:  # bottom-right
            return 2
        elif x == start_x + 1 and y == start_y:  # bottom-left
            return 3
        else:  # top-right
            return 4

    half_size = size // 2
    quad_size = (half_size * half_size)

    # Determine which quadrant (x, y) is in
    if x < start_x + half_size and y < start_y + half_size:  # top-left
        return get_position(n - 1, x, y, start_x, start_y, half_size)
    elif x >= start_x + half_size and y >= start_y + half_size:  # bottom-right
        return quad_size + get_position(n - 1, x, y, start_x + half_size, start_y + half_size, half_size)
    elif x >= start_x + half_size and y < start_y + half_size:  # bottom-left
        return 2 * quad_size + get_position(n - 1, x, y, start_x + half_size, start_y, half_size)
    else:  # top-right
        return 3 * quad_size + get_position(n - 1, x, y, start_x, start_y + half_size, half_size)


def get_coordinates(n, d, start_x, start_y, size):
    """Recursive function to find the coordinates (x, y) of value d."""
    if size == 2:
        # Base case: 2×2 table
        if d == 1:  # top-left
            return start_x, start_y
        elif d == 2:  # bottom-right
            return start_x + 1, start_y + 1
        elif d == 3:  # bottom-left
            return start_x + 1, start_y
        else:  # top-right
            return start_x, start_y + 1

    half_size = size // 2
    quad_size = (half_size * half_size)

    # Determine which quadrant d is in
    if d <= quad_size:  # top-left
        return get_coordinates(n - 1, d, start_x, start_y, half_size)
    elif d <= 2 * quad_size:  # bottom-right
        return get_coordinates(n - 1, d - quad_size, start_x + half_size, start_y + half_size, half_size)
    elif d <= 3 * quad_size:  # bottom-left
        return get_coordinates(n - 1, d - 2 * quad_size, start_x + half_size, start_y, half_size)
    else:  # top-right
        return get_coordinates(n - 1, d - 3 * quad_size, start_x, start_y + half_size, half_size)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        q = int(input())

        for _ in range(q):
            query = input().split()

            if query[0] == "->":
                x, y = int(query[1]), int(query[2])
                result = find_cell_value(n, x, y)
                print(result)
            else:  # "<-"
                d = int(query[1])
                x, y = find_value_position(n, d)
                print(x, y)


if __name__ == "__main__":
    main()