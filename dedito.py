import numpy as np
import matplotlib.pyplot as plt

n =1500
du=0.05
u= np.zeros(n)
R= np.zeros(n)
v= np.zeros(n)
a= np.zeros(n)
P= np.zeros(n)
S= np.zeros(n)
V= np.zeros(n)

def othersolution(R0,v0,e, W0):
     
	R[0]=R0
	v[0]=v0
	u[0]=du
	P[0]=(u[0]**2)*R[0]**2
	S[0]=0
        W[0]=W0
	for i in range(1,n):

		u[i]=u[i-1]+du
		v[i]=v[i-1]-((2./u[i-1])*v[i-1]-(e+(2./u[i-1]))*R[i-1])*(du/2.0)
		R[i]=R[i-1]+v[i]*du
		P[i]=(u[i]**2)*R[i]**2
		S[i]=S[i-1]+P[i-1]*du
                W[i]=W[i-1]+(S[i-1]/u[i-1]
          

	return R



for i in range(1,20):
	q=0.005*i
	plt.figure(i)
	plt.plot(u,othersolution(1,-1,(-1)*q ),label = '$\epsilon=$' + str((-1)*q) ,color='blue')
	plt.legend(loc = 1)
	plt.xlabel("$posicion[s]$")
	plt.ylabel("$Probabilidad$")
	#plt.show()
	plt.savefig('plot'+str(i)+'.jpg')




