'''Enter a signal frequency (Hz). Print "Low Band" (<1000), "Mid Band" (1000–9999), "High Band" (10000–99999), or "Out of Range".
Input: 8000
Output: Mid Band'''

f=int(input())
if f<1000:
    print("Low Band")
elif (f>=1000 & f<=9999):
    print("Mid Band")
elif (f>=10000 & f<=99999):
    print("High Band")
else :
    print("Out f range")