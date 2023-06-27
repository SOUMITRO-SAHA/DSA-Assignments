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


# Optimal Approach:
# TC: O(log n)
# SC: O(1)
def possibleIndex(arr: List[int], target: int) -> int:
    """Binary Search Approach"""
    pans = -1  # This will store the potential index(aka, Position)
    si: int = 0
    ei: int = len(arr) - 1

    while si < ei:
        mid: int = si + (ei - si) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            pans = mid
            si = mid + 1
        else:
            ei = mid - 1

    return pans


def main() -> None:
    """ Default Function"""
    nums_str = input("Enter the Array : ")  # i.e -> [1,3,5,6],
    target = int(input("Enter the Target : "))  # -> 5

    # Converting the Input (String) into int Array:
    nums = convertStringToArray(nums_str)

    if len(nums) >= 1 and type(target) == int:
        res = possibleIndex(nums, target)
        print(res)


# Main Function Start Here:
if __name__ == "__main__":
    # Call the default function
    main()
