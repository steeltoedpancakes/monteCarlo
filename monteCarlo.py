import numpy as np
import matplotlib.pyplot as plt
import math 
import time
import random 


def f(x):
	return np.sin(x)


def g(x):
	return np.cos(x)


def integrate(a,b,N):
    se =0
    so =0    
    dab=(f(a)+f(b))
    h=(b-a)/N
    for i in range(1,N):
        xi=a+h*i
        if i%2==0:
            se=se+2*f(xi)
        else:
            so=so+4*f(xi)
    s=se+so+dab
    return s *(h/3)


def trap(a,b,n):
	x=a
	h=(b-a)/n
	total =0
	for i in range(int(n)):
		total= total+(f(x)+f(x+h))
		x=x+h
	return total*(h/2) 

st=time.time()
x=[]
y=[]
startPoint=0
endPoint=2
for r in np.arange(startPoint,endPoint,.1):
	x.append(r)
	y.append(f(r))
plt.plot(x,y,'-')

xVal=[]
yVal=[]
total=0
n=50000
for r in range (n):
	a=endPoint*random.random()
	b=endPoint*random.random()
	if b<f(a):
		total+=1/n
		xVal.append(a)
		yVal.append(b)

print("the monte carlo function result was ", total, " this result took " ,time.time()-st, " seconds")
st=time.time()
print("the trapazoid method result was  ",trap(startPoint,endPoint,2000) ," this result took " ,time.time()-st, " seconds")
st=time.time()
print("simpsons method produced the result " , integrate(startPoint,endPoint,80)," this result took " ,time.time()-st, " seconds")
plt.plot(xVal,yVal,marker='o',linestyle='')
plt.show()