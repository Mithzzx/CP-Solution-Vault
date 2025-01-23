s = "ABFCACDB"

while "AB" in s or "CD" in s:
    s = s.replace("AB", "").replace("CD", "")
print  (len(s))