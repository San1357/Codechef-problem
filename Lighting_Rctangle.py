'''Problem Code:RECTLIT'''

#CODE:

# cook your dish here

kn=[0,0]
xy=[0,0]

lm=input()
tk=int(lm)
while int(tk)!=0:
    tk-=1
    i=input()
    lin1=0
    lin2=0
    lin3=0
    lin4=0
    ins=0
    kn[0]=int(i.split()[0])
    kn[1]=int(i.split()[1])-1
    out='no'
    
    while kn[0]!=0:
        kn[0]-=1
        j=input()
        xy[0]=int(j.split()[0])
        xy[1]=int(j.split()[1])
        if ((xy[0]==0 and xy[1]==0) or (xy[0]==0 and xy[1]==kn[1]) or (xy[0]==kn[1] and xy[1]==0) or (xy[0]==kn[1] and xy[1]==kn[1])):
            out= 'yes'
            
        elif (xy[0]==0):
            lin1+=1
            if (lin1+lin3)>=2:
                out= 'yes'
                
            elif (((lin1+lin2)>=2 or (lin1+lin4)>=2) and ins>0):
                out= 'yes'
            
            elif ins>=2:
                out= 'yes'
                
                
        elif (xy[1]==0):
            lin2+=1
            if (lin2+lin4)>=2:
                out= 'yes'
                
            elif (((lin2+lin1)>=2 or (lin2+lin3)>=2) and ins>0):
                out= 'yes'
                
            elif ins>=2:
                out= 'yes'
            
        elif (xy[0]==kn[1]):
            lin3+=1
            if (lin1+lin3)>=2:
                out= 'yes'
                
            elif (((lin3+lin2)>=2 or (lin3+lin4)>=2) and ins>0):
                out='yes'
                
            elif ins>=2:
                out= 'yes'
                
        elif (xy[1]==kn[1]):
            lin4+=1
            if (lin2+lin4)>=2:
                out= 'yes'
                
            elif (((lin4+lin1)>=2 or (lin4+lin3)>=2) and ins>0):
                out= 'yes'
                
            elif ins>=2:
                out= 'yes'
                
        else:
            ins+=1
            if (ins>=4):
                out= 'yes'
            elif (((lin4+lin1)>=2 or (lin4+lin3)>=2 or (lin3+lin2)>=2 or (lin1+lin2)>=2) and ins>0):
                out= 'yes'
            
            elif(lin1>0 or lin2>0 or lin3>0 or lin4>0) and ins>1:
                out= 'yes'
    print (out)
