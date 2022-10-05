def replaceElements():
    arr = [17,18,5,4,6,1]
    mx = -1
    for i in range(len(arr) - 1, -1, -1):
        print(f"before: {arr[i]}, {mx}")
        arr[i], mx = mx, max(mx, arr[i])
        print(f"after: {arr[i]}, {mx}")
    return arr


if __name__ == "__main__":
    print(replaceElements())
    