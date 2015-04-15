import numpy as np
import matplotlib.pyplot as plt
import math 
import time
import random 

xVal=[]
yVal=[]
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

def monteCarlo(xRange,yRange,n):
	global xVal,yVal
	area=(xRange[0]+xRange[1])*(xRange[0]+xRange[1])
	total=0
	for r in range (n):
		a=xRange[0]+xRange[1]*random.random()
		b=yRange[0]+yRange[1]*random.random()
		if b<f(a):
			total+=1
			xVal.append(a)
			yVal.append(b)
	return (total/n)*area


xRange=[0,2]
yRange=[0,2]
startPoint=xRange[0]
endPoint=xRange[1]
st=time.time()

print("the monte carlo function result was ", monteCarlo(xRange,yRange,500000), " this result took " ,time.time()-st, " seconds")
st=time.time()
print("the trapazoid method result was  ",trap(startPoint,endPoint,2000) ," this result took " ,time.time()-st, " seconds")
st=time.time()
print("simpsons method produced the result " , integrate(startPoint,endPoint,80)," this result took " ,time.time()-st, " seconds")
x=[]
y=[]
for r in np.arange(startPoint,endPoint,.1):
	x.append(r)
	y.append(f(r))
plt.plot(x,y,'-',color='blue')
plt.plot(xVal,yVal,marker='o',linestyle='',color="green")
plt.show()