#!/usr/bin/env python
import rospy,math,tf 
import math
from std_msgs.msg import Int8
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped,Twist,Vector3,Point,Point32,PoseArray,TransformStamped,PointStamped,PolygonStamped
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import rospkg 
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf import TransformListener 
import tf2_geometry_msgs 
from object_recognition_msgs.msg import RecognizedObjectArray
class GoalPublisher:
    def __init__(self):
        

        self.node_name = rospy.get_name()
        self.tf_listener = TransformListener()
        #self.ped_sub = rospy.Subscriber()
        self.navigation_sub = rospy.Subscriber('/go_object',Int8,self.navigat_callback)
        self.pose_in_map = PointStamped()

    def navigat_callback(self,Data):
        if Data== 1: 
            self.ped_sub = rospy.Subscriber('/object_pos',PointStamped,self.ped_callback)
        else:
            print("wiating for object to be found")
                
    def ped_callback(self,peds_msg):
        print('Im in ped call back')
        try:
            ##now = peds_msg.header.stamp -rospy.Duration(1.0)
            client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
            client.wait_for_server()
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = "map"
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = peds_msg.point.x
            goal.target_pose.pose.position.y =peds_msg.point.y
            goal.target_pose.pose.orientation.w =1.0
            print('Im sending cordinates')
            print(peds_msg.point.x)
            client.send_goal(goal)
            wait = client.wait_for_result()
            if not wait:
                rospy.logerr("Action server not available!")
                rospy.signal_shutdown("Action server not available!")
            else:
                return client.get_result()
        except (tf.LookupException,tf.ConnectivityException,tf.ExtrapolationException):
            print("exception")
        
    def odom_callback(self,odom_msg):  
        print('Im in odom call back')
        
if __name__=='__main__':
    rospy.init_node('GoalPublisher',anonymous=False) 
    print('Im in main')    
    obj=GoalPublisher()
    print('Im after constructor')
    rospy.spin()







