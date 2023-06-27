from typing import List


def convertStringToArray(s: str) -> List[int]:
    # First timing the String
    s = s.strip()

    # Now Checking for '[' and ']'
    if s[0] == '[' and s[len(s) - 1] == ']':
        # Remove the '[' and ']'
        s = s[1:len(s) - 1]
    
    s = s.split(",")
    arr: list[int] = []
    # Converting the String into Array
    for ch in s:
        arr.append(int(ch))

    return arr


# Optimised Approach:
# TC: O(n log n) 
# SC: O(1)
def merge(arr1: List[int], arr2: List[int]) -> None:
    """Two Pointer Approach"""
    m = len(arr1)
    n = len(arr2)
    i = m - 1
    j = 0

    while i >= 0 and j < n:
        if arr1[i] < arr2[j]:
            """Swapping the Element"""
            temp = arr1[i]
            arr1[i] = arr2[j]
            arr2[j] = temp
        j += 1
        i -= 1

    # Sorting the Arrays:
    arr1.sort()


def main() -> None:
    """ Default Function"""
    nums_str1 = input("Enter the Array-1 : ")  # i.e -> [1,2,3,0,0,0],
    nums_str2 = input("Enter the Array-2 : ")  # i.e -> [2,5,6],

    # Converting the Input (String) into int Array:
    nums1 = convertStringToArray(nums_str1)
    nums2 = convertStringToArray(nums_str2)

    if len(nums1) > len(nums2):
        merge(nums1, nums2)
        print(nums1)


# Main Function Start Here:
if __name__ == "__main__":
    # Call the default function
    main()
