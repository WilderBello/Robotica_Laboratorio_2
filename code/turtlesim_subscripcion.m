%rosinit;

sus = rossubscriber('/turtle1/cmd_vel','geometry_msgs/Twist');
pause(1)

sus.LatestMessage

%rosshutdown;
