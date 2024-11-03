def catAndMouse(x, y, z):
    catA = abs(z-x)
    catB = abs(z-y)
    if(catA == catB):
        return "Mouse C"    
    elif(catA < catB):
        return "Cat A"    
    return "Cat B"

catA = int(input("Give me Cat A's position: "))
catB = int(input("Give me Cat B's poition: "))
mouse = int(input("Give me Mouse position: "))

print(catAndMouse(catA, catB, mouse))