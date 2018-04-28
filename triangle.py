import math

def trisquare(a, b, c):
    match = 0
    if a == b:
        match = match + 1
    if a == c:
        match = match + 2
    if b == c:
        match = match + 3
    if (match == 0):
        if( a+b <= c):
            print("Not a triangle")
            return 0.0
        elif(b+c<=a):
            print("Not a triangle")
            return 0.0
        elif(a+c<=b):
            print("Not a triangle")
            return 0.0
        else:
            p = (a+b+c)/2.0
            print("Scalene")
            return math.sqrt(p*(p-a)*(p-b)*(p-c))
    elif(match == 1):
        if(a+b<=c):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a,2)-math.pow(c/2.0,2))
            print("Isosceles")
            return (c*h)/2.0
    elif (match == 2):
        if (a + c <= b):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a, 2) - math.pow(b / 2.0, 2))
            print("Isosceles")
            return (b * h) / 2.0
    elif(match == 3):
        if(b+c<=a):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(b, 2) - math.pow(a / 2.0, 2))
            print("Isosceles")
            return (a*h)/2.0
    else:
        print("Equilateral")
        return(math.sqrt(3.0)*a*a)/4.0

def MU_2_trisquare(a, b, c):
    match = 0
    if a == b:
        match = match + 1
    if a == c:
        match = match + 2
    if b == c:
        match = match + 3
    if (match == 0):
        if( a+b <= c):
            print("Not a triangle")
            return 0.0
        elif(b+c<=a):
            print("Not a triangle")
            return 0.0
        elif(a+c<=b):
            print("Not a triangle")
            return 0.0
        else:
            p = (a+b+c)*2.0
            print("Scalene")
            return math.sqrt(p*(p-a)*(p-b)*(p-c))
    elif(match == 1):
        if(a+b<=c):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a,2)-math.pow(c/2.0,2))
            print("Isosceles")
            return (c*h)/2.0
    elif (match == 2):
        if (a + c <= b):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a, 2) - math.pow(b / 2.0, 2))
            print("Isosceles")
            return (b * h) / 2.0
    elif(match == 3):
        if(b+c<=a):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(b, 2) - math.pow(a / 2.0, 2))
            print("Isosceles")
            return (a*h)/2.0
    else:
        print("Equilateral")
        return(math.sqrt(3.0)*a*a)/4.0


def MU_1_trisquare(a, b, c):
    match = 0
    if a == b:
        match = match + 2
    if a == c:
        match = match + 1
    if b == c:
        match = match + 3
    if (match == 0):
        if( a+b <= c):
            print("Not a triangle")
            return 0.0
        elif(b+c<=a):
            print("Not a triangle")
            return 0.0
        elif(a+c<=b):
            print("Not a triangle")
            return 0.0
        else:
            p = (a+b+c)/2.0
            print("Scalene")
            return math.sqrt(p*(p-a)*(p-b)*(p-c))
    elif(match == 1):
        if(a+b<=c):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a,2)-math.pow(c/2.0,2))
            print("Isosceles")
            return (c*h)/2.0
    elif (match == 2):
        if (a + c <= b):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a, 2) - math.pow(b / 2.0, 2))
            print("Isosceles")
            return (b * h) / 2.0
    elif(match == 3):
        if(b+c<=a):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(b, 2) - math.pow(a / 2.0, 2))
            print("Isosceles")
            return (a*h)/2.0
    else:
        print("Equilateral")
        return(math.sqrt(3.0)*a*a)/4.0

def MU_3_trisquare(a, b, c):
    match = 0
    if a == b:
        match = match + 1
    if a == c:
        match = match + 2
    if b == c:
        match = match + 3
    if (match == 0):
        if( a+b <= c):
            print("Not a triangle")
            return 0.0
        elif(b+c<=a):
            print("Not a triangle")
            return 0.0
        elif(a+c<=b):
            print("Not a triangle")
            return 0.0
        else:
            p = (a+b+c)/2.0
            print("Scalene")
            return math.sqrt(p*(p-a)*(p-b)*(p-c))
    elif(match == 1):
        if(a+b<=c):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a,2)-math.pow(c/2.0,2))
            print("Isosceles")
            return (c*h)*2.0
    elif (match == 2):
        if (a + c <= b):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a, 2) - math.pow(b / 2.0, 2))
            print("Isosceles")
            return (b * h) * 2.0
    elif(match == 3):
        if(b+c<=a):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(b, 2) - math.pow(a / 2.0, 2))
            print("Isosceles")
            return (a*h)*2.0
    else:
        print("Equilateral")
        return(math.sqrt(3.0)*a*a)/4.0

def MU_4_trisquare(a, b, c):
    match = 0
    if a == b:
        match = match + 1
    if a == c:
        match = match + 2
    if b == c:
        match = match + 3
    if (match == 0):
        if( a+b <= c):
            print("Not a triangle")
            return 0.0
        elif(b+c<=a):
            print("Not a triangle")
            return 0.0
        elif(a+c<=b):
            print("Not a triangle")
            return 0.0
        else:
            p = (a+b+c)/2.0
            print("Scalene")
            return math.sqrt(p*(p-a)*(p-b)*(p-c))
    elif(match == 1):
        if(a+b<=c):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a,2)-math.pow(c/2.0,2))
            print("Isosceles")
            return (c*h)/2.0
    elif (match == 2):
        if (a + c <= b):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(a, 2) - math.pow(b / 2.0, 2))
            print("Isosceles")
            return (b * h) / 2.0
    elif(match == 3):
        if(b+c<=a):
            print("Not a triangle")
            return 0.0
        else:
            h = math.sqrt(math.pow(b, 2) - math.pow(a / 2.0, 2))
            print("Isosceles")
            return (a*h)/2.0
    else:
        print("Equilateral")
        return math.sqrt(3.0)*a*a/2.0

LIB = ["trisquare", "MU_1_trisquare", "MU_2_trisquare", "MU_3_trisquare","MU_4_trisquare"]

if __name__=="__main__":
    a = 3.0
    b = 3.0
    c = 3.0
    print(trisquare(a,b,c))
    print(MU_4_trisquare(a, b, c))
