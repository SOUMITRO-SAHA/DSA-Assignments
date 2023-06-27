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
# TC: O(1) => Average Time Complexity
# TC: O(n) => For Special Case.
def addOne(arr: List[int]) -> List[int]:
    extra = 0
    pointer = len(arr) - 1
    while True and pointer >= 0:
        lastDigit = arr[pointer]
        if lastDigit < 9:
            arr[pointer] += 1
            break
        elif lastDigit == 9:
            lastDigit += 1
            extra = lastDigit // 10
            arr[pointer] = lastDigit % 10
            pointer -= 1

    # Very Special Case: When I have to reassign a new Array:
    if arr[0] == 0 and pointer == -1:
        new_arr = [extra]
        for el in arr:
            new_arr.append(el)

        # Assigning the new array to arr:
        arr = new_arr

    return arr


def main() -> None:
    """ Default Function"""
    nums_str = input("Enter the Array : ")  # i.e -> [1,2,3],

    # Converting the Input (String) into int Array:
    nums = convertStringToArray(nums_str)

    if len(nums) >= 1:
        nums = addOne(nums)
        print(nums)


# Main Function Start Here:
if __name__ == "__main__":
    # Call the default function
    main()
