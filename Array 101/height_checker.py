def heightChecker():
    heights = [1,1,4,2,1,3]
    expected = []
    expected.extend(heights)
    expected.sort()
    print(expected)
    count = 0
    for i in range(0, len(heights), 1):
        if heights[i] != expected[i]:
            count += 1
    print(count)


if __name__ == "__main__":
    heightChecker()