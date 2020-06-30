def average(array):
    # your code goes here
    dist = set(array)
    return sum(dist)/len(dist)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)