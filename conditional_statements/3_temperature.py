''' Enter a temperature and print "Overheat" (>75°C), "Normal" (25-75°C), or "Low Temp" (<25°C).
Input: 18
Output: Low Temp'''
temp=int(input())
if temp>75:
    print("Overheat")
elif (temp>=25) and (temp <=75):
    print("Normal")
else:
    print("Low temp")