import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for the left half (invert values to simulate max-heap)
        self.left = []
        # Min-heap for the right half
        self.right = []

    def add_num(self, num: int) -> None:
        # Add to max-heap (left)
        heapq.heappush(self.left, -num)

        # Balance the heaps
        if self.left and self.right and (-self.left[0]) > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        # Maintain size property
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def find_median(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0

# Example usage
median_finder = MedianFinder()
median_finder.add_num(1)
median_finder.add_num(2)
print(median_finder.find_median())  # Output: 1.5
median_finder.add_num(3)
print(median_finder.find_median())  # Output: 2.0
