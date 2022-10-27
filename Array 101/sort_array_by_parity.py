def sortArrayByParity():
    nums = [0]
    p1 = 0
    p2 = len(nums) - 1

    while p1 < p2:
        if nums[p1] % 2 == 0:
            p1 += 1
        if nums[p2] % 2 != 0:
            p2 -= 1
        else:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
    print(nums)


if __name__ == "__main__":
    sortArrayByParity()