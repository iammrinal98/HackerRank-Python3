# Enter your code here. Read input from STDIN. Print output to STDOUT
m, m_list, n, n_list = int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split()))
srt = sorted(m_list.symmetric_difference(n_list))
for x in srt:
    print(x)