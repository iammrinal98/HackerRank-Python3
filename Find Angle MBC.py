from math import atan,degrees
a=int(input())
b=int(input())
k=atan(1.0*a/b)
print (str(int(round(degrees(k))))+'°')