'''Given three boolean flags: `power_on`, `overcurrent`, `overvoltage`, print:
- "System Safe" if only `power_on` is True.
- "Shut Down: Overcurrent" if `overcurrent` is True.
- "Shut Down: Overvoltage" if `overvoltage` is True.
- "Critical Failure" if both faults are True.
Input: True, True, False
Output: Shut Down: Overcurren'''

f1='power-on'
f2='overcurrent'
f3='over_voltage'

if f2:
    print("shutdown:overcurrent")
elif f3:
    print("shutdown:overvoltage")
elif f2 & f3:
    print("Critical failure")
elif f1:
    print("System Safe")
else:
    print("system off")