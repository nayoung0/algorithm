# 2357
import sys
INF = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
min_tree = [INF for _ in range(262144)]
max_tree = [0 for _ in range(262144)]

for _ in range(n):
    l.append(int(input()))

def min_init(node, start, end):
    if start == end:
        min_tree[node] = l[start]
    else:
        mid = (start + end) // 2
        min_tree[node] = min(min_init(node*2, start, mid), min_init(node*2+1, mid+1, end))
    return min_tree[node]

def check_min(node, start, end, left, right):
    if left > end or right < start:
        return INF
    if left <= start and right >= end:
        return min_tree[node]
    mid = (start + end) // 2
    return min(check_min(node*2, start, mid, left, right), check_min(node*2+1, mid+1, end, left, right))

def max_init(node, start, end):
    if start == end:
        max_tree[node] = l[start]
    else:
        mid = (start + end) // 2
        max_tree[node] = max(max_init(node*2, start, mid), max_init(node*2+1, mid+1, end))
    return max_tree[node]

def check_max(node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and right >= end:
        return max_tree[node]
    mid = (start + end) // 2
    return max(check_max(node*2, start, mid, left, right), check_max(node*2+1, mid+1, end, left, right))

min_init(1, 0, n-1)
max_init(1, 0, n-1)

for _ in range(m):
    s, e = map(int, input().split())
    print(check_min(1, 0, n-1, s-1, e-1), check_max(1, 0, n-1, s-1, e-1))