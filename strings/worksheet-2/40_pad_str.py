s=input()
l=len(s)
o_length=int(input())
char=input()
if l<o_length:
    print(char*(o_length-l)+s)