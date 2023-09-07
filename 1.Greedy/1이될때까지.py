n, k = map(int, input().split())
result = 0 

while n >= k :
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1 :
    n -= 1
    result += 1

print(result)

n= 25 k=6

# result = 0

# target = (32 // 7) * 7
# print(target)

# result += (32 - target)
# print(result)