import string


def password_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue
    if count == 3:
        return 'Very Good'
    return 'Weak' if count == 1 else 'Good'


if __name__ == '__main__':
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('qazxswe') == 'Too Weak'
    assert password_strength('QAZXSWE') == 'Too Weak'
    assert password_strength('QAaa1') == 'Too Weak'

    assert password_strength('12345678') == 'Weak'
    assert password_strength('aqwsxcde') == 'Weak'
    assert password_strength('AQWSXCDE') == 'Weak'
    assert password_strength('ZDFGBXDFGBFD') == 'Weak'
    assert password_strength('zsdgvzdsfgzdfg') == 'Weak'

    assert password_strength('1234qwer') == 'Good'
    assert password_strength('1234QWER') == 'Good'
    assert password_strength('QWERqwer') == 'Good'
    assert password_strength('QWERqwersad') == 'Good'

    assert password_strength('1234qwerQEWR') == 'Very Good'
    assert password_strength('1234123123qAr') == 'Very Good'
    assert password_strength('qweqwesA2') == 'Very Good'
    assert password_strength('SADSEDFOI1a') == 'Very Good'
