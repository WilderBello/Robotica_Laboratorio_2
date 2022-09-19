# Entrega Laboratorio 2

El laboratorio 2 de la materia Robótica tiene como objetivo dar una iintroducción a ROS mediante la implementación de un ejemplo de Turtlesim con python y Matlab, esto al poder realizar eñ movimiento de la misma con las teclas WASD.

## Autores

- [Wilder Ofrey Bello Herrera](https://github.com/WilderBello)
- [Javier Eduardo Gutierrez Serrano](https://github.com/jaegutierrezser)

## Solución

Realizando los pasos de la guía dada, se procedió a establecer la conexción con ROS inicialmente para luego realizar las modificaciones planteadas en la guía de desarrollo.

## Descripción de la solución planteada
Dando seguimiento a la guia, se establecieron los siguientes pasos:

<h1>Matlab</h1>

- Dos terminales, en una de ellas lanzar el comando: roscore
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_1.png)
- En la terminal dos lanzar turtlesim con el comando: rosrun turtlesim turtlesim_node
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_2.png)
- Luego se debe iniciar Matlab y crear un script que contenga el código dado en la guía, ejecutar el comando y observar el resultado:
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_3.png)
- Crear un script en Matlab para suscribirse al tópico de pose de la simulación de turtle1:
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_.png)
- Crear un script en Matlab que permita enviar todos los valores asociados a la pose de turtle1.
![](https://github.com/WilderBello/Robotica_Laboratorio_2/blob/main/Imagenes/matlab/Matlab_5.png)
- Para finalizar el nodo maestro se utiliza el comando: clear('master')


* Python
