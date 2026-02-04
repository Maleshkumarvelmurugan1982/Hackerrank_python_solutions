n = int(input())
for _ in range(n):
    a_size = int(input())
    set_a = set(map(int, input().split()))
    b_size = int(input())
    set_b = set(map(int, input().split()))
    print(set_a.issubset(set_b))
