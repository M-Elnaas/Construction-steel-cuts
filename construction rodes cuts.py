#x=[3,7,5,4,5.15,3.3,5,4.5,4]
x=[5.55,3.45,1.75,3,2.35,5,2.20,1.5,3.1,4.32,2.7,4.1]
       
x.sort()
#for i in range(len(x)):
#    x[i]=float(x[i])
print(x)
ini=-1
inii=-1
iniii=-1
iniiii=-1
whole=[]
b=0
for itiration in range(10):
    b=0
#Beginning of looping//////////////////////////////////////////////////////////            
    for i in x:
        if b>=1:
            break
        ini+=1
        if i!=0:
            for ii in x:
                if b>=1:
                    break
                inii+=1
                if inii!=ini and ii!=0:
                    y=i+ii
                    if y==12:
                        whole.append([i,ii])
                        x[ini]=0
                        x[inii]=0
                        b+=1
                        break
                    for iii in x:
                        if b>=1:
                            break
                        iniii+=1
                        if iniii!=inii and iniii!=ini and iii!=0:
                            z=y+iii
                            if z==12:
                                whole.append([i,ii,iii])
                                x[ini]=0
                                x[inii]=0
                                x[iniii]=0
                                b+=1
                                break
                            for iiii in x:
                                iniiii+=1
                                if iniiii!=ini and iniiii!=inii and iniiii!=iniii and iiii!=0:
                                    q=z+iiii
                                    if q==12:
                                        whole.append([i,ii,iii,iiii])
                                        x[ini]=0
                                        x[inii]=0
                                        x[iniii]=0
                                        x[iniiii]=0
                                        b+=1
                                        break
                            iniiii=-1
                    iniii=-1
            inii=-1
    ini=-1


for i in range(len(whole)):
    whole[i].sort()
print(whole)

for itiration in range(10):
    for i in x:
        if i==0:
            x.remove(i)
print(x)





#partial cut optimization

ini=-1
inii=-1
iniii=-1
iniiii=-1
partial=[]
#Beginning of looping//////////////////////////////////////////////////////////            
for i in x:
        ini+=1
        for ii in x:
            inii+=1
            if inii!=ini and ii!=0:
                y=i+ii
                if y<12:
                    for iii in x:
                        iniii+=1
                        if iniii!=inii and iniii!=ini and iii!=0:
                            z=y+iii
                            if z<12:
                                for iiii in x:
                                    iniiii+=1
                                    if iniiii!=ini and iniiii!=inii and iniiii!=iniii and iiii!=0:
                                        q=z+iiii
                                        if q<12:
                                            partial.append([i,ii,iii,iiii,q])
                                iniiii=-1
                    iniii=-1
        inii=-1

for i in range(len(partial)):
    partial[i].sort()


ini=-1
inii=-1
iniii=-1
partial2=[]
#Beginning of looping//////////////////////////////////////////////////////////            
for i in x:
        ini+=1
        for ii in x:
                inii+=1
                if inii!=ini and ii!=0:
                    y=i+ii
                    if y<12:
                        for iii in x:
                            iniii+=1
                            if iniii!=inii and iniii!=ini and iii!=0:
                                z=y+iii
                                if z<12:
                                    partial2.append([i,ii,iii,z])
                        iniii=-1
        inii=-1
        
for i in range(len(partial2)):
    partial2[i].sort()
    
    
    
    
ini=-1
inii=-1
partial3=[]

for i in x:
        ini+=1
        for ii in x:
                inii+=1
                if inii!=ini and ii!=0:
                    y=i+ii
                    if y<12:
                        partial3.append([i,ii,y])
                        
for i in range(len(partial3)):
    partial3[i].sort()
    
    
print(f"The four cuts remaider list:_{partial}")
print(f"\nThe three cuts remaider list:_{partial2}")
print(f"\nThe two cuts remaider list:_{partial3}")

