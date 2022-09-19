import math

def area_of_triangle():
    a = float(input("side a: ")) # asks user for lenght of each side and converts to float type
    b = float(input("side b: "))
    c = float(input("side c: "))
    
    per = float((a + b + c)/2) # calculates half the perimeter
    
    area = round((math.sqrt((per * (per-a) * (per-b) * (per-c)))),2) # uses goven function to calculate area to two decimals
  
    print(area)
    
