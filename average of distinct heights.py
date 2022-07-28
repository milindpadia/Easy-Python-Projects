def average(array):
    heights = set(array)
    sum = 0
    for height in heights:
        sum += height
    average = sum / len(heights)
    return average
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
