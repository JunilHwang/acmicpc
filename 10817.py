s = input().split()
arr = [int(n) for n in s]
middle = None
if arr[0] <= arr[1] <= arr[2] : middle = arr[1]
elif arr[2] <= arr[1] <= arr[0] : middle = arr[1]
elif arr[1] <= arr[2] <= arr[0] : middle = arr[2]
elif arr[0] <= arr[2] <= arr[1] : middle = arr[2]
elif arr[2] <= arr[0] <= arr[1] : middle = arr[0]
elif arr[1] <= arr[0] <= arr[2] : middle = arr[0]
print(middle)