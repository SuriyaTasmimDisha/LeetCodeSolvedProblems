def removeElement():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    i = 0
    n = len(nums)
    while i < n:
        print(n)
        if nums[i] == val:
            print(nums)
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    print(n, nums)


if __name__ == "__main__":
    removeElement()