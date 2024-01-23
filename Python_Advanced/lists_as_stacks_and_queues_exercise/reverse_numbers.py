# numbers = input().split(' ')
# numbers.reverse()
#
# print(*numbers)

from collections import deque

numbers = deque(input().split())

for _ in range(len(numbers)):
    print(numbers.pop(), end=' ')
