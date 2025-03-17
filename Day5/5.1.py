"Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place."

import math

def radians_to_degrees(radians):
    return round(math.degrees(radians), 1)


radian_angle = 1.57  
result = radians_to_degrees(radian_angle)
print("Angle in degrees:", result)
