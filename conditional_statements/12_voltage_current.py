'''Given a voltage and current reading, print "Power OK" if both are in safe ranges, otherwise print specific error:
- Voltage out of 3.0–3.3V: "Voltage Error"
- Current out of 10–500mA: "Current Error"
- Both out: "Power Error"'''

vol=float(input())
cur=int(input())
if (vol<3.0 and vol>3.3):
    print("Voltage Error")
elif (cur <10 and cur >500):
    print("CUrrent Error")
elif ((vol>=3.0 and vol <=3.3) and (cur>=10 and cur<=500)):
    print("Power OK")
else:
    print("Power Error")
