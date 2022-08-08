s="a4c3b2"
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d
output=''.join(sorted(output))
print(output)

