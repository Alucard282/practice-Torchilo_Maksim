import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

print(f"расстояние: {distance(x1,y1,x2,y2): .2f}")