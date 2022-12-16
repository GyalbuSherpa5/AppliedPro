# 1. Remove first n characters from a string. ( use function remove_chars())

def remove_chars(org_str, n):
    mod_string = ""
    for i in range(n, len(org_str)):
        mod_string = mod_string + org_str[i]
    return mod_string


org_str = input("Enter a word ")
n = int(input("Enter a number "))
print(remove_chars(org_str, n))
