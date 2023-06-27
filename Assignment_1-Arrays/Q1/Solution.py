from typing import List, Dict


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
# SC: O(n)
def findTargetSumTwo(nums: list[int], target: int) -> List[int]:
    # Creating a list to store the answer:
    ans: list[int] = []

    # Creating a Dictionary:
    el_map: Dict[int, int] = {}
    i = 0

    # Taking the Elements into the Dictionary
    # {key: element, value:index}
    for el in nums:
        el_map[el] = i
        i += 1

    # Now Searching for the target:
    for el in nums:
        comp = abs(target - el)
        if comp in el_map and el_map[comp] != el:
            ans.append(el_map[el])
            ans.append(el_map[comp])
            break

    return ans


numsStr = input("Enter the Array : ")  # i.e -> [2,7,11,15]
target = int(input("Enter the Target : "))  # -> 9

# Converting the Input into valid Array:
nums = convertStringToArray(numsStr)

if len(nums) >= 2 and type(target) == int:
    res = findTargetSumTwo(nums, target)
    print(res)
