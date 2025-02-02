def palindrome(string):
    if string == string[::-1]:
        return True
    return False

print(palindrome('madam'))
print(palindrome('damsd'))