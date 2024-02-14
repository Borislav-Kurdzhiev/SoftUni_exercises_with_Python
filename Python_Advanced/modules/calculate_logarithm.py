from math import log

number = int(input())

try:
    log_base = int(input())
    print(f'{log(number, log_base):.2f}')
except ValueError:
    print(f'{log(number):.2f}')
