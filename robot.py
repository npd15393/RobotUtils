import math as m
from ik import IK
from jacob import *
import numpy as np
import math
import ikpy
import os
 
class robot:
	def __init__(self,name='irb120'):
		self.urdf=ikpy.chain.Chain.from_urdf_file('./robot.URDF')
		self.dh=[]
		self.home=[]
		self.rho=[]
		if name=='irb120':
			self.IRB120()

	def BuildKineModules(self):
		assert (len(self.dh)>0,'No dh params found')
		#assert( len(self.rho)==len(self.dh),'Specify all joint descriptions')
		#self.IK=IK(self)
		print('Build Success')

	def AddLink(self,alpha,d,a,theta,ro):
		self.dh+=[[alpha,d,a,theta]]
		self.home+=[theta]
		self.rho+=[ro]

	def iterIK(self,xf,qi=None):
 		return (self.urdf.inverse_kinematics([[1, 0, 0, xf[0]],
                             [0, 1, 0, xf[1]],
                             [0, 0, 1, xf[2]],
                             [0, 0, 0, 1]]))
	def IRB120(self):
		self.dh=[]
		self.rho=[]
		self.AddLink(m.pi/2,0.29,0,0,1)
		self.AddLink(0,0,0.27,m.pi/2,1)
		self.AddLink(m.pi/2,0,0.07,0,1)
		self.AddLink(-m.pi/2,0.302,0,0,1)
		self.AddLink(m.pi/2,0,0,0,1)
		self.AddLink(0,0.072,0,m.pi,1)

	def calcDH(self,q):
		assert (len(q)==len(self.rho))
		for qs in range(len(q)):
			self.dh[qs][3]=self.home[qs]
			self.dh[qs][3]+=q[qs]

	def GetEffectorPosition(self,q):
		q=[q1*math.pi/180 for q1 in q]
		self.calcDH(q)
		Tr=ConstructTransform(self.dh)[-1]
		angs=ExtractOrients(Tr[0:3,0:3])
		return np.concatenate((np.dot(Tr,np.array([0,0,0,1]))[0,0:3].reshape([3,1]),angs.reshape([3,1])),axis=0)


	def SetEffectorPosition(self,xf):
		return self.iterIK(xf)
