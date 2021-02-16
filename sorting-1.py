from sys import stdin

# 머지 소트 사용 가능
# def merge_sort(array):
#     if len(array) <= 1:
#         return array
#     mid = len(array) // 2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])

#     i, j, k = 0, 0, 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             array[k] = left[i]
#             i += 1
#         else:
#             array[k] = right[j]
#             j += 1
#         k += 1
    
#     if i == len(left):
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
#     elif j == len(right):
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
#     return array

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(stdin.readline()))

# 머지 소트 사용하는 경우
# numbers = merge_sort(numbers)

# 근데 머지 소트보다 속도가 빠름
# 머지 소트: 7752ms
# sorted: 1368ms
for i in sorted(numbers):
    print(i)