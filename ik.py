import numpy as np
from jacob import Jacobian
import ikpy


class IK:
	global lamda
	lamda=0.1
	def __init__(self,robot):
 		self.robot=robot
 		self.chain = robot.urdf

	def iterIK(self,xf,qi=None):
 		return (self.chain.inverse_kinematics([[1, 0, 0, xf[0]],
                             [0, 1, 0, xf[1]],
                             [0, 0, 1, xf[2]],
                             [0, 0, 0, 1]]))

	def IterJInv(self,xf,qi=None):
 		if qi is None:
 			qi=np.zeros([len(self.robot.rho),1])
 		
 		J=Jacobian(self.robot.dh,self.robot.rho)
 		Jpinv=np.transpose(J)
 		while np.abs(np.linalg.norm(np.dot(Jpinv,qi)-xf))>0.001:
 			self.robot.calcDH(qi)
 			J=Jacobian(self.robot.dh,self.robot.rho)
 			#Jpinv=np.dot(np.transpose(J),np.linalg.inv((lamda**2)*np.identity(6)+np.dot(J,np.transpose(J))))
 			Jpinv=np.transpose(J)
 			Jg=np.dot(Jpinv,(xf-np.dot(J,qi)).reshape(6,1))
 			qi+=0.2*Jg
 			print(np.linalg.norm(np.dot(Jpinv,qi)-xf))
 		return qi

	def CCD(self,xf,qi):
 		pass
