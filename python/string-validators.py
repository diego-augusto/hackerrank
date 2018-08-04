if __name__ == '__main__':
    s = input()

    has_alphanumeric = False
    has_alphabetical = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False

    for letter in s:
        if letter.isalnum():
            has_alphanumeric = True
        if letter.isalpha():
            has_alphabetical = True
        if letter.isdigit():
            has_digits = True
        if letter.islower():
            has_lowercase = True
        if letter.isupper():
            has_uppercase = True

    print(has_alphanumeric)
    print(has_alphabetical)
    print(has_digits)
    print(has_lowercase)
    print(has_uppercase)
