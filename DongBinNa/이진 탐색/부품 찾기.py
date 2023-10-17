n = int(input())

array = set(map(int,input().split()))

m = int(input())

x= list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes', end=" ")
    else:
        print('no', end=" ")

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
#
#
# n = int(input())
# array = list(map(int, input().split()))
#
# m = int(input())
# goods = list(map(int, input().split()))
#
# for i in goods:
#     res = binary_search(array, i, 0, n - 1)
#     if res == None:
#         print("no", end=" ")
#     else:
#         print("yes", end=" ")