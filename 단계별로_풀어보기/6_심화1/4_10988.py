word=list(input())
word_reverse=[]
for i in reversed(word):
    word_reverse.append(i)
"".join(word)
"".join(word_reverse)
if word == word_reverse:
    print("1")
else:
    print("0")