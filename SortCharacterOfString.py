
s=input(str("Enter Some Alphanumric String to sort:"))
Alphabat=[]
Digits=[]
for ch in s:
    if ch.isalpha():
        Alphabat.append(ch)
    else:
        Digits.append(ch)
output=''.join(sorted(Alphabat)+sorted(Digits))
print(output)