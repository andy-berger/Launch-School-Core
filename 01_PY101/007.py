def short_long_short(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    if s1_length < s2_length:
        return s1 + s2 + s1
    else:
        return s2 + s1 + s2

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
