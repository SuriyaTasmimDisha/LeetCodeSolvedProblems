def containsDuplicate(nums):
    convertedNums = set(nums)
    print(type(convertedNums))
    print(convertedNums)
    if len(convertedNums) == len(nums):
        return True
    else:
        return False

containsDuplicate([1,2,3,3,4])