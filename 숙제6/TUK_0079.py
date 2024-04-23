def remove_characters(string_a, string_b):
    for char in string_b:
        string_a = string_a.replace(char, '')
    return string_a

string_a = input()
string_b = input()

result = remove_characters(string_a, string_b)
print(result)