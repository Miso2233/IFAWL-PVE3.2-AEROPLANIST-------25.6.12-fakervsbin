import time,random

while 1:
    dt=0.03
    e = random.randint(33,66)
    stri="-"*e + "+"
    t1=0
    tm=time.time()
    for m in range(len(stri)):
        try:
            print(stri[m],end="")
            time.sleep(0)
        except:
            pass
    print()
    t0=time.time()
    for i in range(100):
        try:
            print("|",end="")
            time.sleep(dt)
        except:
            t1=time.time()
            break
    t=t1-t0
    if dt*(e+1) +t0-tm< t < dt*(e+5)+t0-tm:
        print("x")
        print("fire!")
    else:
        print("?")
