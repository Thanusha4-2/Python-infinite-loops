n=1
sc=0
while n>0:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        summ+=fact
    if n==summ:
        sc+=1
    if sc==10:
        print(n)
        break
    n+=1
    
