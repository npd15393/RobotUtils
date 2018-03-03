import numpy as np
from jacob import Jacobian

 class IK:
 	def __init__(self,robot):
 		self.J=Jacobian(robot.dh,robot.rho)

 	def IterJInv(self,xf,qi):
 		if qi is None:
 			qi=np.zeros(self.J.shape[1])
 		del=np.inf

 		while del>0.001:
 			del=np.dot(np.transpose(J),np.dot(J,np.transpose(J)))
 			qi+=del

 		return qi

 	def CCD(self,xf,qi):
 		pass