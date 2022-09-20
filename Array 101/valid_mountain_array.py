def validMountainArray():
    arr = [3,5,5]
    l_p = 0
    max_index = 0
    if len(arr) < 3:
        return False
    for i in range(1, len(arr), 1):
        if arr[l_p] < arr[i]:
            l_p += 1
        else:
            max_index = l_p
            break
    print(max_index)
    if max_index == 0 or max_index == len(arr) - 1:
        return False
    for i in range(max_index, len(arr)-1, 1):
        if arr[i] <= arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(validMountainArray())
