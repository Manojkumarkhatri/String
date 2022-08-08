s="Hello I am Manoj Kumar"
l=s.split() #['Hello','I','am','Manoj','Kumar']
l1=[]
for word in l:
    l1.append(word[::-1])
l1=' '.join(l1)
print(l1)