from operator import le
from numpy import insert


def main():
    arr = [8, 4, 5,0, 0,0, 0, 7]
    length = len(arr)
    i = 0
    while i < length:
        if arr[i] == 0:
            arr.insert(i+1, 0)
            i += 2
        else: i += 1
        if len(arr) > length:
            arr.pop()
    print(arr)


if __name__ == "__main__":
    main()
