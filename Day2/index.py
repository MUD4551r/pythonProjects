km = float(input("Enter Distance in Km : "))
miles = (km * 0.62137119)

print(f"{km} (km) distance in miles is {miles} (miles)")

if miles > 0:
    print("distance is positive")
elif miles < 0:
    print("distance is negative")
else:
    print("distance  is Zero")
    
if km > miles:
    print("the digit of KM is larger")
elif miles > km :
    print("the digit of miles is larger")
else:
    print("the digit of km == miles")
    
# radius print area of a circle
import math
r = float(input("Enter radius of circle : "))
area = math.pi * r**2
print("area of circle : ", area)