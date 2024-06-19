import re

regex_integer_in_range = r'^[1-9]\d{5}$'
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'


def is_valid_postal_code(postal_code):
    if not re.match(regex_integer_in_range, postal_code):
        return False
    alternating_repetitive_pairs = re.findall(regex_alternating_repetitive_digit_pair, postal_code)
    return len(alternating_repetitive_pairs) <= 1



postal_codes = ["121626", "523563", "552523", "123456", "987654", "123123"]
for code in postal_codes:
    print(f"{code}: {is_valid_postal_code(code)}")
