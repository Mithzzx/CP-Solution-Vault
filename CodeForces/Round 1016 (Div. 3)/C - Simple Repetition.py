def gcd(a, b):
    """Find greatest common divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    """Check if a number is prime using Miller-Rabin primality test for specific bounds"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # For smaller numbers, use trial division which is faster
    if n < 10000:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    # Implementation of Miller-Rabin primality test
    # For n < 2^64, these bases are enough for deterministic primality testing
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    # Write n-1 as d*2^r by factoring out powers of 2
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for a in bases:
        if a >= n:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def check_repetition_primality(x, k):
    """Determine if repeating x k times creates a prime number using mathematical properties"""
    # Case 1: If k > 1 and x ends with 0, 2, 4, 6, or 8, the result is always divisible by 2
    if k > 1 and x % 10 in [0, 2, 4, 6, 8]:
        return False

    # Case 2: If k > 1 and x ends with 5, the result is always divisible by 5
    if k > 1 and x % 10 == 5:
        return False

    # Case 3: If x = 1, the result is a repunit (all 1s)
    if x == 1:
        # Repunits are prime only for specific prime values of k
        # For the range 1 ≤ k ≤ 7, only k=2 and k=19 are known to produce prime repunits
        # Since k ≤ 7, we only need to check k=2
        return k == 2  # 11 is prime

    # For k=1, just check if x itself is prime
    if k == 1:
        return is_prime(x)

    # For remaining cases, create the number and check primality
    y = int(str(x) * k)

    # Check if the number is divisible by 9 (sum of digits divisible by 9)
    digit_sum = sum(int(digit) for digit in str(y))
    if digit_sum % 9 == 0:
        return False

    # If x has a common factor with 10, and k > 1, the result is not prime
    if k > 1 and gcd(x, 10) > 1:
        return False

    # For all other cases, check primality
    return is_prime(y)


def main():
    t = int(input())
    for _ in range(t):
        x, k = map(int, input().split())
        print("YES" if check_repetition_primality(x, k) else "NO")


if __name__ == "__main__":
    main()