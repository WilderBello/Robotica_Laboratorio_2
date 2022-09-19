%rosinit;

showdetails(sus.LatestMessage) %Revisamos el valor de la posición de manera completa en cada eje y el ang.

%Ingresar los datos de movimiento
X = 2;
Y = 3;
AngZ = -1;

velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Crea el publicador
velMsg = rosmessage(velPub); %Crea el mensaje

velMsg.Linear.X = X;
velMsg.Linear.Y = Y;
velMsg.Angular.Z = AngZ;

send(velPub, velMsg); %Envia los datos


sus = rossubscriber('/turtle1/cmd_vel','geometry_msgs/Twist');
pause(1)

sus.LatestMessage

showdetails(sus.LatestMessage)

%rosshutdown;