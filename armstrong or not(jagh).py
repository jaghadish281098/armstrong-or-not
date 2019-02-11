n=int(raw_input())
tot=0
while(n>0):
    t=n%10
    tot=tot+pow(t,3)
    n=n//10
print tot
if tot==n:
    print "armstrong"
else:
    print "not armstrong"
