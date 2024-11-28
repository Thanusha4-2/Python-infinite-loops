ll=int(input())
ul=int(input())
for n in range(ll,ul+1):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ=summ+rem
    if n%summ==0:
        print(n)
    n+=1
    
