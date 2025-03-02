s = input()
s = s.lower()
if len(s)%2==0:
    if s == s[::-1]:
        print("palindrome")
    else: print("not palindrome")
else: print("not palindrome")