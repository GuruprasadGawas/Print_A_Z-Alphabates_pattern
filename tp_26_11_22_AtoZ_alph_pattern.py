height = 5
width = 2 * height

def printA():
    n = width//2
    for i in range(0,height):
        for k in range(3):
            for j in range(0, width):
                if (i ==0 and j==n) or (i==1 and j==n-1) or (i==1 and j==n+1)or (i ==2 and (j>=n-2 and j <= n+2)) or (i== height-2 and (j== 2 or j==width-2)) or (i==height-1 and (j==1 or j==width-1)) :
                    print("*",end="")
                else:
                    print(" ",end="")
            print("",end='')
        print('')
    

def printB():
    n = width//2
    for i in range(0,height):
        for j in range(0,width):
            if j==0 or ((i==0 or i==2 or i==height-1)and j<=width-2) or ((i==1 or i==height-2) and j==width-1):
                print("*",end="")
            else:
                print(" ",end="")
        print("")
     

def printC():
    for i in range(0,height):
        for j in range(0,width):
            if ((i==0 or i==height-1) and (j>1 and j<width-2)) or ((i==1 or i==height-2 or i==height//2) and j==0):
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    

def printD():
    n = width//2
    for i in range(0,height):
        for j in range(0,width):
            if j==0 or ((i==0 or i==4)and j<=width-3) or ((i==1 or i==height-2) and j==width-2) or (i==2 and j== width-1):
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    

def printE():
    for i in range(height):
        for j in range(width):
            if j==0 or i==0 or i==height//2 or i==height-1:
                print("*",end='')
            else:
                print(' ',end='')
        print('')
    

def printF():
    for i in range(height):
        for j in range(width):
            if j==0 or i==0 or i==height//2:
                print("*",end='')
            else:
                print(' ',end='')
        print('')
    
def printG():
    for i in range(height):
        for j in range(width):
            if ((i==0 or i==height-1) and (j>1 and j<width-2)) or ((i==1 or i==height-2 or i==height//2) and j==0) or ((i==height//2 or i==height-2) and (j==width-1 )) or (i==height//2 and (j==width-3 or j==width-2)):
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    

def printH():
    for i in range(0,height):
        for j in range(0,width):
            if j==0 or j==width-1 or i==height//2:
                print('*',end='')
            else:  
                print(' ',end='')
        print('')
    

def printI():
    n = width//2
    for i in range(height):
        for j in range(width-1):
            if i==0 or i==height-1 or j==n-1:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printJ():
    n = width//2
    for i in range(height):
        for j in range(width-1):
            if i==0 or ((i==height-1) and (j>=1 and j<=n-2)) or (j==n-1 and i!=height-1) or (i==height-2 and j==0):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printK():
    n = width//2
    for i in range(height):
        for j in range(width):
            if ((i==0 or i==height-1) and j==n-1) or ((i==1 or i==height-2) and j==n-2) or j==0 or (i==height//2 and j==1):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printL():
    n = width//2
    for i in range(height):
        for j in range(width):
            if j==0 or (i==height-1 and j<=n):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printM():
    n = width//2-1
    for i in range(height):
        for j in range(width-1):
            if j==0 or ((j==1 or j==width-3) and i==1) or (i==height//2 and (j==2 or j==width-4)) or (i==3 and (j==3 or j== width-5)) or (i==height-1 and j==n) or j==width-2:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printN():
    n = width//2-1
    for i in range(height):
        for j in range(width-1):
            if j==0 or j==width-2 or (i==height//2 and j==n) or (i==1 and j==n//2) or (i== height-2 and j==width-4):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printO():
    n = width//2-1
    for i in range(height):
        for j in range(width-1):
            if (i==height//2 and (j==0 or j==width-2)) or ((i==0 or i==height-1) and(j==n-1 or j==n+1)) or ((i==1 or i==height-2) and (j==1 or j==width-3)):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
      


def printP():
    n = width//2
    for i in range(height):
        for j in range(width-1):
            if j==0 or ((i==0 or i==height//2) and j<=n-1) or (i==1 and j==n):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printQ():
    n = width//2-1
    for i in range(height):
        for j in range(width):
            if (i==height//2 and (j==0 or j==width-2)) or ((i==0 or i==height-1) and(j==n-1 or j==n+1)) or ((i==1 or i==height-2) and (j==1 or j==width-3)) or (i==height//2 and j==n+1) or (i==height-1 and j==width-1):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    
def printR():
    n = width//2-1 
    for i in range(height):
        for j in range(width):
            if j==0 or ((i==0 or i==height//2) and j<=n-1) or (i==1 and j==n) or (i==height-2 and j==n-2) or (i==height-1 and j==n):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printS():
    n = width//2-1
    for i in range(height):
        for j in range(width-1):
            if ((i==0 or i==height//2 or i==height-1) and(j>=n-2 and j<=n+2)) or (i==1 and j==1 ) or (i==height-2 and j==width-3):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printT():
    n = width//2
    for i in range(height):
        for j in range(width-1):
            if i==0 or j==n-1:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    
def printU():
    n = width//2
    for i in range(height):
        for j in range(width-1):
            if (j==0 and i!=height-1) or (i==height-1 and (j>=1 and j<=width-3)) or (j==width-2 and i!=height-1):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printV():
    n = width//2
    for i in range(0,height):
        for j in range(0, width):
            if (i==height-1 and j==n) or (i==height-2 and j==n-2) or (i==height-2 and j==n+2) or (i== height//2 and (j== 2 or j==width-2)) or ((i==0 or i==1) and (j==1 or j==width-1)) :
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    

def printW():
    n = width//2-1
    for i in range(height):
        for j in range(width-1):
            if j==0 or ((j==1 or j==width-3) and i==height-2) or (i==height//2 and (j==2 or j==width-4)) or (i==1 and (j==3 or j== width-5)) or (i==0 and j==n) or j==width-2:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    

def printX():
    n = width//2-1
    for i in range(height):
        for j in range(width-1):
            if (i==0 and (j==0 or j==width-2)) or (i==height-1 and (j==0 or j==width-2)) or (i==height//2 and j==n) or (i==1 and (j==n-2 or j==n+2)) or (i==height-2 and (j==n-2 or j==n+2)):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    
    

def printY():
    n = width//2-1
    for i in range(height):
        for j in range(width-1):
            if (i==0 and (j==0 or j==width-2)) or (j==n and (i>=height//2 and i<=height-1)) or (i==1 and (j==n-2 or j==n+2)):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    


def printZ():
    n=width//2-1
    for i in range(height):
        for j in range(width-1):
            if i==0 or i==height-1 or (i==height//2 and j==n) or (i==1 and j==n+2) or (i==height-2 and j==n-2):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    
print("-----!------!----Print the A-Z alphabate * pattern----!------!------")
while True:
    alphaIn = input("Enter any of the \'A-Z\' alphabate to print * pattern and enter 'Exit' for stop the printing: ")
    if alphaIn == 'A':
        printA()
    elif alphaIn == 'B':
        printB()
    elif alphaIn == 'C':
        printC()
    elif alphaIn == 'D':
        printD()
    elif alphaIn == 'E':
        printE()
    elif alphaIn == 'F':
        printF()
    elif alphaIn == 'G':
        printG()
    elif alphaIn == 'H':
        printH()
    elif alphaIn == 'I':
        printI()
    elif alphaIn == 'J':
        printJ()
    elif alphaIn == 'K':
        printK()
    elif alphaIn == 'L':
        printL()
    elif alphaIn == 'M':
        printM()
    elif alphaIn == 'N':
        printN()
    elif alphaIn == 'O':
        printO()
    elif alphaIn == 'P':
        printP()
    elif alphaIn == 'Q':
        printQ()
    elif alphaIn == 'R':
        printR()
    elif alphaIn == 'S':
        printS()
    elif alphaIn == 'T':
        printT()
    elif alphaIn == 'U':
        printU()
    elif alphaIn == 'V':
        printV()
    elif alphaIn == 'W':
        printW()
    elif alphaIn == 'X':
        printX()
    elif alphaIn == 'Y':
        printY()
    elif alphaIn == 'Z':
        printZ()
    elif alphaIn == 'Exit':
        exit()
    else:
        print('please, Enter a alphabate...')
