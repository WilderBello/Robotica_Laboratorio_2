import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi
from pynput import keyboard as kb

def pulsa(tecla):
    print('\n Se ha pulsado la tecla {}'.format(tecla))
    if tecla == kb.KeyCode.from_char('t'):
        return False
    if tecla == kb.KeyCode.from_char('w'):
        pubVel(1,0,0.1)
    if tecla == kb.KeyCode.from_char('s'):
        pubVel(-1,0,0.1)
    if tecla == kb.KeyCode.from_char('d'):
        pubVel(0,1,0.1)
    if tecla == kb.KeyCode.from_char('a'):
        pubVel(0,-1,0.1)
    if tecla == kb.KeyCode.from_char('r'):
        reset(0,0,0.1)
    if tecla == kb.KeyCode.from_char('Key.space'):
        pubVel(0,10,0.1)

def reset(x, y, t):
    pub = rospy.Publisher('/turtle1/teleport_absolute', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    rospy.service('/turtle1/teleport_absolute')
    vel = Twist()
    vel.linear.x = x
    vel.linear.y = y
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

def pubVel(vel_x, ang_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.angular.z = ang_z
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

if __name__ == '__main__':
    pubVel(0,0,0.1)
    try:
        kb.Listener(pulsa).run()
    except rospy.ROSInterruptException:
        pass