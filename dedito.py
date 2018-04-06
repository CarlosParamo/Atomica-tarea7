import numpy as np
import matplotlib.pyplot as plt

n =1500
du=0.05
u= np.zeros(n)
RA= np.zeros(n)
vA= np.zeros(n)
RB= np.zeros(n)
vB= np.zeros(n)
a= np.zeros(n)
P= np.zeros(n)
S= np.zeros(n)
W= np.zeros(n)

def othersolution(R0,v0,e, W0):
     
	RA[0]=R0
	vA[0]=v0
	RB[0]=R0
	vB[0]=v0
	u[0]=du
	P[0]=(u[0]**2)*RA[0]**2
	S[0]=0
        W[0]=W0
	for i in range(1,n):

		u[i]=u[i-1]+du
		vA[i]=vA[i-1]-((2./u[i-1])*vA[i-1]-(e-(1./u[i-1]))*RA[i-1])*(du/2.0)
		RA[i]=RA[i-1]+vA[i]*du
		P[i]=(u[i]**2)*RA[i]**2
		S[i]=S[i-1]+P[i-1]*du
                
		#Potencial que sufre B
		W[i]=W[i-1]+(S[i-1]/u[i-1]**2)-2./u[i-1]

		#solucion a schrodinger para B
		vB[i]=vB[i-1]-((2./u[i-1])*vB[i-1]-(e-W[i]/4.)*RB[i-1])*(du/2.0)
		RB[i]=RB[i-1]+vB[i]*du



		
   
	return W

plt.plot(u,othersolution(1,-1,(-1), 1),label = '$\epsilon=$' + str((-1)) ,color='green')
plt.savefig('plotlok.jpg')

for i in range(1,20):
	q=0.1+0.1*i
	plt.figure(i)
	plt.plot(u,othersolution(1,-1,(-1)*q,1 ),label = '$\epsilon=$' + str((-1)*q) ,color='blue')
	plt.legend(loc = 1)
	plt.xlabel("$posicion[s]$")
	plt.ylabel("$Probabilidad$")
	#plt.show()
	plt.savefig('plot'+str(i)+'.jpg')




