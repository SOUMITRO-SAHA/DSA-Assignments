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


# Brute-Force Approach:
# TC: O(n)
# SC: O(1)
def findNumber(arr: List[int]) -> List[int]:
    rep = 0
    n = len(arr)
    arr_sum = 0
    act_sum = int((n * (n + 1)) / 2)

    # Finding the total Sum of all the array elements
    prev = 0
    for i in range(len(arr)):
        arr_sum += arr[i]
        if arr[prev] == arr[i] and i > 0 and rep == 0:
            rep = arr[i]

        if i != 0:
            prev += 1

    diff = abs(act_sum - arr_sum)
    # Formula: original_num = diff + rep

    return [rep, (diff + rep)]


def main() -> None:
    """ Default Function"""
    nums_str = input("Enter the Array : ")  # i.e ->  [1,2,2,4]

    # Converting the Input (String) into int Array:
    nums = convertStringToArray(nums_str)

    if len(nums) >= 1:
        nums = findNumber(nums)
        print(nums)


# Main Function Start Here:
if __name__ == "__main__":
    # Call the default function
    main()
