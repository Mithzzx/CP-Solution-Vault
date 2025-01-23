sentence1 ="of"
sentence2 ="A lot of words"

if len(sentence1) < len(sentence2):
    sentence1, sentence2 = sentence2, sentence1
sentence1 = set(sentence1.split())
sentence2 = set(sentence2.split())

print(sentence1)
for i in sentence2:
    if i not in sentence1:
        print(i,"not in",sentence1)
        print("False")
        break
else:
    print(True)