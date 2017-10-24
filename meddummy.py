import sys
for x in range(5):
    a = int(input())
    print("MedPY got : "+str(a), file=sys.stderr)
    if x%2==0:
        print(a**2)
    else: print(a+2)

    
