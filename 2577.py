s = str(int(input()) * int(input()) * int(input()))
arr = [0] * 10
for v in s : arr[int(v)] += 1
for v in arr : print(v)