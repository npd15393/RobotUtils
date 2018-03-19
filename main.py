from robot import robot
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from geometry_msgs.msg import Point
import time as t
import math as m
t0=t.time()

class rosact(object):
    def __init__(self):
        rospy.init_node('act')
        self.pubs=[]
        self.pubs.append(rospy.Publisher('/irb120/joint_1_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/irb120/joint_2_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/irb120/joint_3_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/irb120/joint_4_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/irb120/joint_5_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/irb120/joint_6_position_controller/command',Float64,queue_size=10))
        rospy.sleep(1)

    def write(self,pos):
        while True:
            x=0.1*m.cos(t.time()-t0)
            y=0.1*sin(t.time()-t0)
            pos=self.robot.iterIK(x,y)
            msg=Float64() 
            print('Writing ')
            print(pos)
            for i in range(len(pos)):
                msg.data=pos[i]+(time.time()-t0)/180 if i==4 else pos[i]
                self.pubs[i].publish(msg)
            #rospy.sleep(0.01)

def main():
    self.robot=robot('irb120')
    self.robot.BuildKineModules()
    #jts=[30,0,0,0,10+time.time()-t0,0]
    a=self.robot.GetEffectorPosition(jts)
    print(a)
    #print(t.SetEffectorPosition(a[0,0:6]))
    act=rosact()
    act.write(jts)
    print('this shouldnt be displayed')

if __name__== '__main__':
    main()

