a=input("enter string:")
charactercount=0
wordcount=1
for i in a:
    charactercount+=1
    if (i==' '):
        wordcount+=1
print("number of words in the string")
print(wordcount)
print("number of characters in the string")
print(charactercount)
