import numpy as np
import math as m

def Jacobian(dh,rho):

	T=ConstructTransform(dh)

	t=ExtractOrients(T[-1][0:3,0:3])

	zs=[np.dot(t,np.array([0,0,1,1]))[0,0:3] for t in T]

	On=np.dot(T[-1],np.array([0,0,0,1]))

	Os=[(On-np.dot(T[i],np.array([0,0,0,1])))[0,0:3] for i in range(len(T))]

	j=np.zeros([6,len(zs)])

	for l in range(len(zs)):
		j[:,l]=np.concatenate((np.cross(zs[l][0,0:3],Os[l][0,0:3]).reshape([3,1]),zs[l][0,0:3].reshape([3,1])),axis=0).reshape([6]) if rho[l]==1 else np.concatenate((zs[l][0,0:3].reshape([3,1]),np.zeros([3,1])),axis=0).reshape([6])

	return np.matrix(j)


def ConstructTransform(dh):
	T=[np.identity(4)]
	for l in dh:
		T+=[np.dot( np.matrix(T[-1]),np.matrix([[m.cos(l[3]),-m.sin(l[3])*m.cos(l[0]),m.sin(l[3])*m.sin(l[0]), l[2]*m.cos(l[3])],\
						[m.sin(l[3]), m.cos(l[3])*m.cos(l[0]), -m.cos(l[3])*m.sin(l[0]), l[2]*m.sin(l[3])],\
						[0, m.sin(l[0]),m.cos(l[0]),l[1]],\
						[0,0,0,1]]))]
	T.pop(0)
	return T



def ExtractOrients(R):
	t1=m.atan2(R[2,1],R[2,2])
	t2=m.atan2(-R[2,0],m.sqrt(R[2,1]**2+R[2,2]**2))
	t3=m.atan2(R[1,0],R[0,0])
	return np.array([t1,t2,t3])