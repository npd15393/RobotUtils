import numpy as np
from jacob import Jacobian

 class IK:
 	def __init__(self,robot):
 		self.J=Jacobian(robot.dh,robot.rho)

 	def IterJInv(self,xf,qi):
 		if qi is None:
 			qi=np.zeros(self.J.shape[1])
 		
 		Jinv=np.transpose(self.J)

 		while np.abs(np.dot(Jinv,qi)-xf)>0.001:
 			Jinv=np.dot(np.transpose(J),np.dot(J,np.transpose(J)))
 			qi+=Jinv

 		return qi

 	def CCD(self,xf,qi):
 		pass