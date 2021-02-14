# Note:
# Problem Code :ADTCHP 



n,m,q=map(int,input().split())
l=[]
for i in range(q):
    a,x1,y1,x2,y2=map(int,input().split())
    if a==1:
        l.append([list([x1,y1]),list([x2,y2])])
    if a==2:
        for i in range(len(l)):
            if l[i][0][0]>=x1 and l[i][0][1]>y1 and l[i][1][0]<x2 and l[i][1][0]<y2:
                print("YES")
            elif l[i][0][0]>x1 and l[i][0][1]>=y1 and l[i][1][0]<x2 and l[i][1][0]<y2:
                print("YES")
            elif l[i][0][0]>x1 and l[i][0][1]>y1 and l[i][1][0]<=x2 and l[i][1][0]<y2:
                print("YES")
            elif l[i][0][0]>x1 and l[i][0][1]>y1 and l[i][1][0]<x2 and l[i][1][0]<=y2:
                print("YES")
            elif l[i][0][0]<=x1 and l[i][0][1]<y1 and l[i][1][0]>x2 and l[i][1][1]>y2:
                print("YES")
            elif l[i][0][0]<x1 and l[i][0][1]<=y1 and l[i][1][0]>x2 and l[i][1][1]>y2:
                print("YES")
            elif l[i][0][0]<x1 and l[i][0][1]<y1 and l[i][1][0]>=x2 and l[i][1][1]>y2:
                print("YES")
            elif l[i][0][0]<x1 and l[i][0][1]<y1 and l[i][1][0]>x2 and l[i][1][1]>=y2:
                print("YES")
            elif l[i][0][0]==x1 and l[i][0][1]==y1 and l[i][1][0]==x2 and l[i][1][1]==y2:
                print("YES")
            else:
                print("NO")
