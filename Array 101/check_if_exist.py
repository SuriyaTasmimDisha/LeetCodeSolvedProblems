def checkIfExist():
    arr = [10, 5, 2, 0]
    nums = set()
    for i in arr:
        if i*2 in nums or i/2 in nums:
            return True
        nums.add(i)
    return False

if __name__ == "__main__":
    print(checkIfExist())