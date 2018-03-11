from robot import robot
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from geometry_msgs.msg import Point

class rosact(object):
    def __init__(self):
        rospy.init_node('act')
        self.pubs=[]
        self.pubs.append(rospy.Publisher('/joint_1_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/joint_2_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/joint_3_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/joint_4_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/joint_5_position_controller/command',Float64,queue_size=10))
        self.pubs.append(rospy.Publisher('/joint_6_position_controller/command',Float64,queue_size=10))
        rospy.sleep(1)

    def write(self,pos):
        while True:
            msg=Float64() 
            print('Writing ')
            print(pos)
            for i in range(len(pos)):
                msg.data=pos[i]
                self.pubs[i].publish(msg)
            rospy.sleep(0.01)

def main():
    t=robot('irb120')
    t.BuildKineModules()

    jts=[30,0,20,0,10,0]
    a=t.GetEffectorPosition(jts)
    print(a)
    #print(t.SetEffectorPosition(a[0,0:6]))
    act=rosact()
    act.write(jts)
    print('this shouldnt be displayed')

if __name__== '__main__':
    main()

