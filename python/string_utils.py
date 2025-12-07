
def to_upper(s):
    return s.upper()

def count_chars(s):
    return len(s)

def is_palindrome(s):
    cleaned_s = ''.join(filter(str.isalnum, s)).lower()
    return cleaned_s == cleaned_s[::-1]
