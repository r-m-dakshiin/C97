


introString=input("Enter String : ")
characterCount=0
wordcount=0
for i in introString:
    characterCount=characterCount+1
    if (i==' '):
        wordcount=wordcount+1
print("No. of words in the string:")
print(wordcount)
print("No. of characters in the string:")
print(characterCount)
