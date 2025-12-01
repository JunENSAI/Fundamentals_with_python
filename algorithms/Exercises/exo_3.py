import time

def search_rotate(nums, target):
    """
    Finds the index of target in a rotated sorted array.
    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

def run_tests():
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4, "Standard Rotation"),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1, "Target Not Found"),
        ([1], 0, -1, "Single Element (Missing)"),
        ([1], 1, 0, "Single Element (Found)"),
        ([1, 3], 3, 1, "Two Elements"),
        ([5, 1, 3], 5, 0, "Pivot at index 1"),
        ([1, 2, 3, 4, 5], 4, 3, "Not Rotated (Standard Binary Search)"),
    ]

    print(f"{'Description':<35} | {'Passed':<8} | {'Result'}")
    print("-" * 60)

    for nums, target, expected, desc in test_cases:
        result = search_rotate(nums, target)
        passed = "YES" if result == expected else "NO"
        print(f"{desc:<35} | {passed:<8} | Expected {expected}, Got {result}")

if __name__ == "__main__":
    run_tests()