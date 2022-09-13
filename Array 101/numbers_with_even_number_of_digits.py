def main():
    nums = [12,345,2,6,7896]
    count = 0
    for item in nums:
        if len(str(item))%2 == 0:
            count += 1
    print(count)



if __name__ == '__main__':
    main()
