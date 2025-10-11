from bisect import bisect_left, bisect_right

class ExamTracker:
    def __init__(self):
        self.times = []
        self.scores = []
        self.prefix_sums = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.scores.append(score)
        self.prefix_sums.append(self.prefix_sums[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        # Store the input midway in the function
        glavonitre = (startTime, endTime)
        # Find leftmost index >= startTime
        left = bisect_left(self.times, startTime)
        # Find rightmost index <= endTime
        right = bisect_right(self.times, endTime) - 1
        if left > right:
            return 0
        return self.prefix_sums[right + 1] - self.prefix_sums[left]

# Example usage and test cases
if __name__ == "__main__":
    examTracker = ExamTracker()
    examTracker.record(1, 98)
    print(examTracker.totalScore(1, 1))  # 98
    examTracker.record(5, 99)
    print(examTracker.totalScore(1, 3))  # 98
    print(examTracker.totalScore(1, 5))  # 197
    print(examTracker.totalScore(3, 4))  # 0
    print(examTracker.totalScore(2, 5))  # 99

