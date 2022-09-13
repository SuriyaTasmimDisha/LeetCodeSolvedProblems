from unittest import result


def main():
    nums = [1,1,0,1,1,1]
    # count = 0
    # result = 0
    # current_count = 0
    # for i, ele in enumerate(nums):
    #         if nums[i] == 1:
    #             current_count = current_count + 1
    #         if (nums[i] != 1 or len(nums) == i + 1) and current_count > count:
    #             count = current_count
    #             current_count = 0
    #     return count
    # for i, item in enumerate(nums):
    #     if nums[i] == 1:
    #         current_count = current_count + 1
    #         count = max(current_count, count)
    #     else:
    #         current_count = 0
    # print(f'count {count}, {current_count}')

    # for item in nums:
    #     if item == 1:
    #         count += 1
    #     else:
    #         result = max(count, result)
    #         count = 0
    count = 0
    result = 0
    for item in nums:
        if item == 1:
            count += 1
        else:
            result = max(count, result)
            count = 0
    result = max(count, result)
    print(result)


if __name__ == '__main__':
    main()
