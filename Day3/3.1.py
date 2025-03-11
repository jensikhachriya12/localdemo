"Write a Program that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points."
import math

def calculate_distance(x1, y1, x2, y2):
     distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
     return distance

x1,y1=map(float,input("Enter of point 1 (x1,y1): ".split()))
x2,y2=map(float,input("Enetr of point 2 (x2,y2): ".split()))

distance=calculate_distance(x1,y1,x2,y2)

print("The distance point of:",distance)

