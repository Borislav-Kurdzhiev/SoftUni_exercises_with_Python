occurrences = {}

for letter in input():
    occurrences[letter] = occurrences.get(letter, 0) + 1
for symbol, times in sorted(occurrences.items()):
    print(f'{symbol}: {times} time/s')

# solution No 2
# text = input()
# for symbol in sorted(text):
#     print(f'{symbol}: {text.count(symbol)} time/s')
