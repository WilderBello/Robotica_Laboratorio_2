rosshutdown;
rosinit;

velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Crea el publicador
velMsg = rosmessage(velPub); %Crea el mensaje

velMsg.Linear.X = 1; %Valor del mensaje
send(velPub, velMsg); %Envia los datos
pause(1)


