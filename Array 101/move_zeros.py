def moveZeroes():
    nums = [-1,1,0,0,8,0,-2,0,3]
    index_of_zero = -1
    is_zero = True
    for i in range(0,len(nums),1):
        if nums[i] == 0 and is_zero:
            index_of_zero = i
            is_zero = False
        elif index_of_zero > -1 and nums[i] != 0:
            nums[index_of_zero], nums[i] = nums[i], 0
            index_of_zero =  index_of_zero + 1
        print(nums)


if __name__ == "__main__":
    moveZeroes()