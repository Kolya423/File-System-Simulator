Two Heaps Approach:

Max-heap (left) → stores the smaller half of numbers.
Min-heap (right) → stores the larger half of numbers.
Add Number:

Insert into max-heap (left), then balance heaps:
If the max of left is greater than the min of right, swap values.
Ensure left heap size is always >= right heap size.
Find Median:

If left is larger, median is top of left.
If equal size, median is average of tops.
Key Idea:
Keep numbers split into two balanced halves using heaps for O(log n) operations.
