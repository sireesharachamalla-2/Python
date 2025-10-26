'''Given three sensor readings, print "Majority High" if at least two readings are above a threshold (e.g., 50), otherwise "Majority Low".
Input: 40, 65, 70
Output: Majority High'''
s1=int(input())
s2=int(input())
s3=int(input())
th=50
high=(s1>th)+(s2>th)+(s3>th)
if(high>=2):
    print("majority High")
else:
    print("Majority Low")
