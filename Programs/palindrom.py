def palindrom(s):
    pal_str = ''
    pal_len = 0
    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > pal_len:
                pal_str = s[left:right + 1]
                pal_len = right - left + 1
            left -= 1
            right += 1
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > pal_len:
                pal_str = s[left:right + 1]
                pal_len = right - left + 1
            left -= 1
            right += 1
    return pal_str


print(palindrom('fdfdfd'))
