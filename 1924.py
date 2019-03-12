months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
s = input().split(' ')
x = int(s[0])
y = int(s[1])
month = months[x - 1]
n = 0
for v in months[:x-1] : n+=v
n += y
print(days[n % 7])