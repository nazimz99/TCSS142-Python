#Nazim Zerrouki
x = int(input("Enter the value for the x component. "))
print("You entered", x, "for the x component.")
y = int(input("Enter the value for the y component. "))
print("You entered", y, "for the y component.")
z = int(input("Enter the value for the z component. "))
print("You entered", z, "for the z component.")
if x > 0:
    if y > 0 and z > 0:
       print("You are in Octant I.")
    elif y < 0 and z > 0:
       print("You are in Octant IV.")
    elif y > 0 and z < 0:
       print("You are in Octant V.")
    elif y < 0 and z < 0:
       print("You are in Octant VIII.")
    elif y == 0 and z == 0:
        print("Your point lies on the x-axis.")
    elif y == 0:
       print("Your point lies on the xz plane.")
    else:
       print("Your point lies on the xy plane.")
elif x < 0:
    if y > 0 and z > 0:
        print("You are in Octant II.")
    elif y < 0 and z > 0:
        print("You are in Octant III.")
    elif y > 0 and z < 0:
        print("You are in Octant VI.")
    elif y < 0 and z < 0:
        print("You are in Octant VII.")
    elif y == 0 and z == 0:
        print("Your point lies on the x-axis.")
    elif y == 0:
        print("Your point lies on the xz plane.")
    else:
        print("Your point lies on the xy plane.")
elif x == 0:
    if y != 0 and z != 0:
        print("Your point lies on the yz plane.")
    elif y != 0 and z == 0:
        print("Your point lies on the y-axis.")
    elif y == 0 and z != 0:
        print("Your point lies on the z-axis.")
    else:
        print("Your point lies at the origin.")
