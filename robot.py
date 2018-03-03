import math as m
from ik import IK

class robot:
	def __init__(self,name='irb120'):
		if nameis None:
			self.dh=[]
			self.rho=[]
		else:
			IRB120()

	def BuildKineModules(self):
		assert (len(dh)>0,'No dh params found')
		assert( len(rho)==len(dh),'Specify all joint descriptions')
		self.IK=IK(self)

	def AddLink(alpha,d,a,theta,ro):
		self.dh+=[alpha,a,d,theta]
		self.rho+=ro

	def IRB120(self):
		AddLink(m.pi/2,0.29,0,0)
		AddLink(0,0,0.27,m.pi/2)
		AddLink(m.pi/2,0,0.07,0)
		AddLink(-m.pi/2,0.302,0)
		AddLink(m.pi/2,0,0,0)
		AddLink(0,0.072,0,0)

	def calcDH(self,q):
		for qi in range(len(q)):
			self.dh[qs][3]=q[qi]

	





