import math
def aproximate_pi(n): # takes an integer >2 number of sides as parameter 'n'
    theta = math.radians(360/n) # calculates, in radians, the central angle of each partitioned triangle
    height = ((math.cos((theta/2)))) # calcules the height of the triangle
    half_apothem = (math.sin((theta/2))) # calculates half the base of the triangle
    
    
    area = (n * height * half_apothem) #calculates the area using simplied formula of a triangle times n triangles
   
    print(area)
     
