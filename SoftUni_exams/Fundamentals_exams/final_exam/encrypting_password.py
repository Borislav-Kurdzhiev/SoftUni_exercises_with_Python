import re

pattern = r'^(\S+)>(?P<numbers>[0-9]{3})\|(?P<lowerCaseLetters>[a-z]{3})\|(?P<upperCaseLetters>[A-Z]{3})\|(?P<symbols>[^<>]{3})<\1$'


def main():
    numberOfLines = int(input())
    for _ in range(numberOfLines):
        tryPass = input()
        match = re.match(pattern, tryPass)

        if match:
            encryptedPass = (
                    match.group('numbers') +
                    match.group('lowerCaseLetters') +
                    match.group('upperCaseLetters') +
                    match.group('symbols')
            )
            print(f"Password: {encryptedPass}")
        else:
            print("Try another password!")


if __name__ == "__main__":
    main()
