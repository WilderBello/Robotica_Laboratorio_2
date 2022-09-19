# Entrega Laboratorio 2

El laboratorio 2 de la materia Robótica tiene como objetivo dar una introducción a ROS mediante la implementación de un ejemplo de Turtlesim con python y Matlab, esto al poder realizar eñ movimiento de la misma con las teclas WASD.

## Autores

- [Wilder Ofrey Bello Herrera](https://github.com/WilderBello)
- [Javier Eduardo Gutierrez Serrano](https://github.com/jaegutierrezser)

## Solución

Realizando los pasos de la guía dada, se procedió a establecer la conexción con ROS inicialmente para luego realizar las modificaciones planteadas en la guía de desarrollo.

## Descripción de la solución planteada
Dando seguimiento a la guia, se establecieron los siguientes pasos:

<h3>Matlab</h3>

- Dos terminales, en una de ellas lanzar el comando: roscore
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_1.png)
- En la terminal dos lanzar turtlesim con el comando: rosrun turtlesim turtlesim_node
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_2.png)
- Luego se debe iniciar Matlab y crear un script que contenga el código dado en la guía, ejecutar el comando y observar el resultado:
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_3.png)
- Crear un script en Matlab para suscribirse al tópico de pose de la simulación de turtle1:
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_4.png)
- Crear un script en Matlab que permita enviar todos los valores asociados a la pose de turtle1.
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_5.png)
- Para finalizar el nodo maestro se utiliza el comando: clear('master')


<h3> Python </h3>

Escribir un código que permita operar una tortuga del paquete turtlesim con el teclado, de tal manera que: se mueva hacia adelante y hacia atrás con W y S, debe girar en sentido horario y antihorario con las teclas D y A, debe retornar a su posoción y orientación centrales con la tecla R y debe dar un giro de 180 grados con la tecla espacio.

- Código desarrollado en Python:

![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/python/Python_1.png)

![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/python/Python_2.png)

- Posteriormente se agregó el script a CMakeLists.txt como se puede observar en la imagen:

![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/python/Python_3.png)

- Al realizar el catkin_make se obtuvo el siguiente error:

![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/python/Python_4.png)

Por lo que se procedió a ejecutar el script directamente de la consola de vscode, obteniendo así los resultados esperados:

![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/python/Python_5.png)
