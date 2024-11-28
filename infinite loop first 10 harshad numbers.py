n=1
hc=0
while True:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ=summ+rem
    if n%summ==0:
        print(n)
        hc+=1
    if hc==10:
        break
    n+=1
    
