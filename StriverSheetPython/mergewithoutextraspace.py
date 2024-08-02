#first way tc: o(nlogn + mlogm + min(n, m)) =>O(nlogn)

a1,a2= [1,3,5,7],[0,2,6,8,9]

i,j=len(a1)-1,0
while i>=0 and j<len(a2):
    if a1[i]>a2[j]:
        a1[i],a2[j]=a2[j],a1[i]
    i-=1;j+=1

a1.sort()
a2.sort()
#print(a1,a2)

a1,a2= [1,3,5,7],[0,2,6,8,9]


#gap method

gap= (len(a1) + len(a2) + 1)//2

while gap>0:
    l=0;r=l+gap
    while r<(len(a1)+len(a2)):
        if l<len(a1) and r>=len(a1):
            if a1[l]>a2[r-len(a1)]:
                a1[l],a2[r-len(a1)]=a2[r-len(a1)],a1[l]
                
        elif l>=len(a1):
            a1[l-len(a1)],a2[r-len(a1)]=a2[r-len(a1)],a1[l-len(a1)]
             
        else:
            a1[l],a2[r]=a2[r],a1[l]
        l+=1;r+=1
    if gap == 1:
        break
    gap=(gap+1)/2

print(a1,a2)
            