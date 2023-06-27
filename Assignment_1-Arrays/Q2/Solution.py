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


# Better Approach:
# TC: O(n)
# SC: O(1)
def removeValFromArray(arr: List[int], val: int) -> None:
    """Two Pointer Approach"""
    si = 0
    ei = 0
    while len(arr) > ei:
        while len(arr) > si and arr[si] != val:
            si += 1

        # If the si reached to the target Value: then start the ei from that point
        if si < len(arr) and arr[si] == val:
            ei = si

        while len(arr) > ei and arr[ei] == val:
            ei += 1

        if (len(arr) > ei > si and si < len(arr)
                and arr[si] == val and arr[ei] != val):
            '''Swapping'''
            arr[ei], arr[si] = arr[si], arr[ei]

    # After Swapping, Updating the Value of ei to -1
    for i in range(len(arr)):
        if arr[i] == val:
            arr[i] = -1


def default_function():
    """ Default Function"""
    nums_str = input("Enter the Array : ")  # i.e -> [3,2,2,3],
    val = int(input("Enter the Target : "))  # -> 3

    # Converting the Input into valid Array:
    nums = convertStringToArray(nums_str)

    # Changeling for Valid input:
    if type(val) == int:
        removeValFromArray(nums, val)
        print(nums)


# Main Function Start Here:
if __name__ == "__main__":
    # Call the default function
    default_function()
