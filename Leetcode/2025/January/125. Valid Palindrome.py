s = "A man, a plan, a canal: Panama"
s = s.lower()
s = ''.join(e for e in s if e.isalnum())
print(s == s[::-1])