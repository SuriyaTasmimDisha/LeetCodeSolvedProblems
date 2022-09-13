def heapify(arr, n, i):
    largest = i #Take i as largest node
    print('largest: ', i)
    l_side = 2 * i + 1
    print('l_side: ', l_side)
    r_side = 2 * i + 2
    print('r_side: ', r_side)
    if l_side < n and arr[l_side] > arr[largest]:
        largest = l_side
        print('l_largest: ', largest)
    if r_side < n and arr[r_side] > arr[largest]:
        largest = r_side
        print('r_largest: ', largest)

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print('i: ' + str(arr[i]) + ' largest: ' + str(arr[largest]))
        print(arr)
        heapify(arr, n, largest)


def heapsort(arr):
    print(arr)
    n = len(arr)

    # Step 1: Create a Max Heap
    # Last Parent node at (n//2)-1 position
    for i in range(n // 2 - 1, -1, -1):
        print('index: ', i)
        heapify(arr, n, i)
    
    # Extract and sort element
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        print('sort: ', arr)
        heapify(arr, i, 0)

    print('final array: ', arr)

arrayList = [12, 13, 4, 5, 6, 20]
# heapsort(arrayList)
# print(bin(1))
a = 1
b = bin(0)
print(type(b))
if b:
    print('Hi a')
else:
    print('hi B')

