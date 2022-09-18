def removeDuplicates():
    nums = [0,0,1,1,1,2,2,3,3,4]
    p = 1
    for i in range(1, len(nums), 1):
        if nums[i-1] != nums[i]:
            nums[p] = nums[i]
            p += 1
    print(nums, p)

if __name__ == "__main__":
    removeDuplicates()
