s = input("Enter a string: ")

first_char = s[0]
result = first_char

for i in range(1, len(s)):
    if s[i] == first_char:
        result += '$'
    else:
        result += s[i]

print("Modified string:", result)
