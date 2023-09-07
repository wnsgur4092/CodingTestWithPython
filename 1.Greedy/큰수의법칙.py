n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k  #count 1
print("count1:", count)

count += m % (k + 1)  #count 2
print("count2:", count)

result = 0
result += (count) * first
print("result:", result)

result += (m-count) * second
print("result2:", result)

print(result)