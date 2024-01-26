nums =int(input())

primary_sum, secondary_sum = 0, 0

for i in range(nums):
    line = [int(x) for x in input().split()]
    primary_sum += line[i]
    secondary_sum += line[nums - i - 1]

print(abs(primary_sum - secondary_sum))
        