def main():
    nums = [-12, -11, -7, -6, -4, -2, -1, 0, 3, 10]
    n = len(nums)
    new_list = [0] * n
    left_pointer = 0
    right_pointer = n-1
    for i in range(n-1, -1, -1):
        if abs(nums[left_pointer]) > abs(nums[right_pointer]):
            square = nums[left_pointer]
            left_pointer += 1
        else:
            square = nums[right_pointer]
            right_pointer -= 1
        new_list[i] = square ** 2
    print(new_list)


if __name__ == '__main__':
    main()
