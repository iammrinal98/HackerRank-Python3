# Enter your code here. Read input from STDIN. Print output to STDOUT
n_m = input().split()
n_m = map(int, n_m)
n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

counter = 0
for i in n:
    if i in A:
        counter += 1
    elif i in B:
        counter -= 1
print(counter)