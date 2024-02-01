from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


VALID_DOMAINS = ('.com, .bg, .org, .net')
min_name_symbols_counter = 4

pattern_name = r'\w+'

email = input()

while email != 'End':

    if email.count('@') > 1:
        raise MoreThanOneAtSymbol('Email should contain only one @ symbol')
    elif '@' not in email:
        raise MustContainAtSymbolError('Email should contain @ symbol')
    elif len(email.split('@')[0]) <= min_name_symbols_counter:
        raise NameTooShortError('Name must be more than 4 characters')
    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f'Domain must be one of the following: {"".join(el for el in VALID_DOMAINS)}')
    elif findall(pattern_name, email.split('@')[0])[0] != email.split('@')[0]:
        raise InvalidNameError('Name must contain only letters, digits and underscores')

    email = input()
