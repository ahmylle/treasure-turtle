from turtle import *
# Target Area
target_x = 50
target_y = 40
target_range = 30   # How close they need to be

# Function to Check Hit (returns a boolean)
def hit_target(x, y):
    return abs(x - target_x) < target_range and abs(y - target_y) < target_range

# write your pseudocode below
#slecting the coordinates to travle to 
#if statment to check if the coordinates are within the target range
x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))
if hit_target(x, y):
    
        print("Hit!")
        penup()
        goto(x,y)
        pendown()
        color("green")
        begin_fill()
        circle(20)
        end_fill()
        
        
else:
        print("Miss!")
        penup()
        goto(x,y)
        pendown()
        color("red")
        begin_fill()
        circle(20)
        end_fill()

done()



