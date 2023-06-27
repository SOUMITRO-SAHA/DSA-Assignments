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
# SC: O(n) => In Worst Case.
def findDuplicate(arr: List[int]) -> bool:
    """Hash-Table"""
    fq: dict[int, int] = {}

    # Taking the frequencies of elements into the hash-table
    for el in arr:
        if el in fq:
            # Duplicate Found:
            return True
        else:
            fq[el] = 1

    return False


def main() -> None:
    """ Default Function"""
    nums_str = input("Enter the Array : ")  # i.e -> [1,2,3,1]

    # Converting the Input (String) into int Array:
    nums = convertStringToArray(nums_str)

    if len(nums) >= 1:
        nums = findDuplicate(nums)
        print(nums)


# Main Function Start Here:
if __name__ == "__main__":
    # Call the default function
    main()
