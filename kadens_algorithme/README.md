## Kadane’s Algorithm

### Kadane’s Algorithm is a popular and efficient way to solve the maximum subarray sum problem. Given an array of numbers (which may include both positive and negative values), the goal is to find the contiguous subarray with the largest possible sum.

Instead of checking every possible subarray (which would be slow), Kadane’s Algorithm works in a single pass through the array by tracking two values:

    - Current Sum: the maximum sum of the subarray ending at the current position.
    - Max Sum: the best (largest) sum found so far.

At each step, it decides whether to:

    - extend the current subarray, or start a new one at the current element.
    - This makes the algorithm very fast and efficient (O(n) time complexity).

It’s often used in interview questions and real-world applications where performance matters.

