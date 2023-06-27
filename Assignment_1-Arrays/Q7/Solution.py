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


# Optimal Solution
# TC: O(n)
# SC: O(1)
def move_zeros_to_end(arr: List[int]) -> None:
    si = 0
    ei = 0
    while ei < len(arr):
        while ei < len(arr) and arr[ei] == 0:
            ei += 1
        # Now, the ei stands in a non-zero element:
        while si < len(arr) and arr[si] != 0:
            si += 1
        # Now the si stands in a zero element

        # Checking for Valid Swapping:
        if si < len(arr) and ei < len(arr) and arr[si] == 0 and arr[ei] != 0:
            # Now, Swap them:
            arr[si], arr[ei] = arr[ei], arr[si]

        ei += 1


def main() -> None:
    """ Default Function"""
    nums_str = input("Enter the Array : ")  # i.e -> [0,1,0,3,12]

    # Converting the Input (String) into int Array:
    nums = convertStringToArray(nums_str)

    if len(nums) >= 1:
        move_zeros_to_end(nums)
        print(nums)


# Main Function Start Here:
if __name__ == "__main__":
    # Call the default function
    main()
