text=input()
size=int(input())
chunks=[]
for i in range(0,len(text),size):
    chunks.append(text[i:i+size])
print(chunks)