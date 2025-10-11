def hasEqualScoreSubstrings(s: str) -> bool:
    # Calculate total score of the string
    total_score = sum(ord(char) - ord('a') + 1 for char in s)

    # If total score is odd, we cannot split into two equal parts
    if total_score % 2 != 0:
        return False

    target_score = total_score // 2
    left_score = 0

    # Try all possible split points (i goes from 0 to n-2)
    # This ensures both parts are non-empty
    for i in range(len(s) - 1):
        left_score += ord(s[i]) - ord('a') + 1

        # If left score equals target, we found a valid split
        if left_score == target_score:
            return True

        # If left score exceeds target, no point continuing
        if left_score > target_score:
            break

    return False