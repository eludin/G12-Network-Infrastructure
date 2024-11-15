##DISTANCE CONVERTER:
import math

#Percentage length relative to 9 inches, multiplied by correct length magnitude
def  vertical(x):
    true = (x/9)*42
    return true

def horizontal(y):
    true = (y/13)*65
    return true

##Note: The X and Y have different conversion factors,
##Requires you to convert both seperatly and then combine using pythagorean
def other(x,y):
    trueX = (x/9)*42
    trueY = (y/13)*65
    true = math.sqrt(trueX**2 + trueY**2)
    return true


def area(x,y):
    trueX = (x/9)*42
    trueY = (y/13)*65
    area = trueX*trueY
    return area



while(True):
    
    choice = input("What Type of Line:\nVertical:1\nHorizontal:2\nOther Line:3\nSquare:4\n")

    if choice == "1":
        vertLen = float(input("How long does visio say? "))
        print("Length=",round(vertical(vertLen),2),"[m]")
    if choice == "2":
        horzLen = float(input("How long does visio say? "))
        print("Length=",round(horizontal(horzLen),2),"[m]")
    if choice == "3":
        Lenx = float(input("HORIZONTAL Distance in visio: "))
        Leny = float(input("VERTICAL Distance in visio: "))
        print("Length=",round(other(Lenx,Leny),2),"[m]")
    if choice == "4":
        Lenx = float(input("HORIZONTAL Distance in visio: "))
        Leny = float(input("VERTICAL Distance in visio: "))
        print("TOTAL AREA=",round(area(Lenx,Leny),2),"[m^2]")
    print("\n\n")
