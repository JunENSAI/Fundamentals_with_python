## Binary Search on a Rotated Array

You are given a sorted list of integers that has been "rotated" at an unknown pivot index (e.g., ``). Write a function search(nums, target) that returns the index of the target.

- **Constraint**: You cannot simply iterate the list, as that is O(n). The solution must be O(log n).

- **Logic**: A standard binary search checks the middle element. In a rotated array, at least one half (left or right) remains sorted. The algorithm must determine which side is sorted, check if the target lies within that range, and then adjust the low or high pointers accordingly.

- **Significance**: This tests the ability to reason logically about index manipulation and dividing the problem space, a key skill for scalable algorithm design. 