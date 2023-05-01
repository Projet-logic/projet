



def exist_in_list(l,i,j):
    for circle in l:
        if(circle[0]==i and circle[1]==j):
            return circle[2]
    else:
        return False
    
def print_instance(list_of_c,n,m):
    print(" ",end="")
    for i in range(m):
        print("---",end="")
    print(" ",end="")
    print()
    for j in range(n):
        print('|',end="")
        index=0
        j2=2
        while j2<(m*3)+1:
            index+=(j2%3 == 1)
            
            n=exist_in_list(list_of_c, j, index)
            if(n):
                print(f'({n})',end="")
                j2+=3
            else:
                print(' ',end="")
                j2+=1
        print('|')
    print(" ",end="")
    for i in range(m):
        print("---",end="")
    print(" ",end="")
    print()
    
def init_game():
    try:
        n=int(input("enter width of grid"))
    except:
        print("you should have entered a number")
        return 0
    while(not(1<n<=10)):
        try:
            n=int(input("width should be between 1 and 10 enter width of grid"))
        except:
            print("you should have entered a number")
            return 0
        
    try:
        m=int(input("enter length of grid"))
    except:
        print("you should have entered a number")
        return 0
    while(not(1<n<=10)):
        try:
            m=int(input("length should be between 1 and 10 enter width of grid"))
        except:
            print("you should have entered a number")
            return 0
    
    res=input("do you want to add a circle?(y/n)")
    while(res!='y' and res!='n'):
        res=input("do you want to add a circle?(y/n)")
    l=list()
    while (res!='n'):
        
        try:
            i=int(input("insert row number"))
        except:
            print("you should have entered a number")
            return 0
        
        while(not(1<=i<=n)):
            try:
                i=int(input(f"row should be between 1 and {n} enter width of grid"))
            except:
                print("you should have entered a number")
                return 0
        try:
            j=int(input("insert colunm number"))
        except:
            print("you should have entered a number")
            return 0
        
        while(not(1<=i<=m)):
            try:
                j=int(input(f"colunm should be between 1 and {m} enter width of grid"))
            except:
                print("you should have entered a number")
                return 0
        try:
            bn=int(input("insert bridg limited number"))
        except:
            print("you should have entered a number")
            return 0
        
        while(not(1<=i<=8)):
            try:
                bn=int(input("bridg limited number should be between 1 and 8 enter width of grid"))
            except:
                print("you should have entered a number")
                return 0
        
        l.append((i,j,bn))
        print_instance(l, n, m)
        res=input("do you want to add a circle?(y/n)")
        while(res!='y' and res!='n'):
            res=input("do you want to add a circle?(y/n)")
    print("by ;)")
    return l,n,m
    
        