# Practica-final---Modelado-y-simulaci-n-de-robots

## 1º Robot en rviz

El robot cuenta con dos cámaras , una delante y otra en la pinza que enfoca al cubo. Las TFs están orientadas tal que todos los giros de las articulaciones son en el eje z, y la base y el footprint en el robot cumplen con la orientación propiesta en el REP-103 (x forward y left z up), así como los optical frames de las cámaras (z forward x right y down), salvo en la del brazo, que está configurada para mirar hacia abajo.

Podemos ver las articulaciones, los frames, y las imágenes de ambas cámaras en la siguiente imagen:

<img width="1453" height="940" alt="imagen" src="https://github.com/user-attachments/assets/114f5539-9469-4e2b-9511-d72fbfa3c9a7" />

Para ver el sentido positivo de los giros de las articulaciones, podemos modular la posición de la articulación con el nodo: *joint_state_publisher_gui*, que podemos incluir en nuestro launch de la siguiente forma:

``` python3
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time
        }]
    )

    ld = LaunchDescription()
    ld.add_action(joint_state_publisher_gui_node)
```

Por ejemplo los del brazo:

<img width="1451" height="918" alt="imagen" src="https://github.com/user-attachments/assets/5f1a7a5c-d0b0-4a39-8060-5879ea78a993" />

Por último, podemos ver los frames del robot en la siguiente imágen:

<img width="1832" height="800" alt="imagen" src="https://github.com/user-attachments/assets/5351b269-1348-46b8-8806-bc41bf3f6921" />

O en el pdf: *frames_2026-04-26_19.00.35.pdf* dentro de la carpeta *data*

## 2º Objetivo de la simulación

El robot debe de coger el cubo verde y depositarlo en el maletero. Después debe orientarse hacia el cubo azul, cogerlo, y moverlo hasta el cubo rojo para depositarlo encima (si puede), y luego debe de avanzar unos metros.

Para ello me he ayudado del paquete *teleop_twist_keyboard*, aparte del framework de *Moveit2*, para configurar las poses del robot. El video de la simulación es el siguiente: 

https://github.com/user-attachments/assets/22664e53-6c85-47b9-80b3-4c69ac9ce682

## 3º Resultados

Mientras realizaba la simulación, se grababan los topics: /imu, /joint_states y /cmd_vel en una rosbag, que se encuentra en *data* con el nombre *results*. Gracias a esto he podido realizar las siguientes gráficas:


### 1- Aceleración vs tiempo


<img width="999" height="578" alt="imagen" src="https://github.com/user-attachments/assets/2b336393-9192-4f52-8c01-8102be76dfe7" />


Como podemos ver, la aceleración del robot se estabiliza en 0 en x y en y cuando está en reposo (antes de moverse hacia el cubo azul, cuando está cogiendo el cubo azul y cuando lo deja sobre el rojo), justo el comportamiento que esperábamos.

Sin embargo, vemos como se estabiliza a 9,8 en z, ya que el imu esta viendo todo el peso de la gravedad.

### 2- Posición de las ruedas vs tiempo


<img width="1004" height="581" alt="imagen" src="https://github.com/user-attachments/assets/ca55e82e-9a91-4487-9897-27034045afd4" />

Esta gráfica se complementa muy bien con la anterior, ya que lo que medimos no es la posición como tal, sino el giro de las ruedas. 
Como apunte, el robot ha estado diseñado para verse desde alante, por eso las ruedas de la derecha son las del lado izquierdo, si se ve desde atrás.
Tanto las de la izquierda como las de la derecha tienen el z positivo orientado de la misma manera, esto hace que si el robot avanza recto, todas los giros suben, pero cuando el robot gira, como ejerce velocidad negativa a unas ruedas y positva a otras, unos giros suben y otros bajan. Es exactamente el comportamiento que vemos. El robot antes de girar tiene todas sus ruedas giradas 0 rad, y cuando gira hacia la izquierda, las ruedas de la derecha (izquierda si lo vemos desde atrás), giran en sentido negativo, y las otras en positivo. Estos offsets que se crean, tanto al orientarse hacia el cubo azul como al orientarse hacia el cubo rojo, son los que hacen que luego cuando avance recto, las ruedas aumenten su giro de manera proporcional, pero con cierta distancia.

### 3- G-parcial del brazo + gripper


<img width="998" height="582" alt="imagen" src="https://github.com/user-attachments/assets/5f5bd0e8-5085-4b20-a8cc-c428aea216ca" />


Vemos esta gráfica donde se nota claramente cuando el robot agarra el cubo y cuando no. Como el robot intenta mantener la posición del brazo cuando está en movimiento, vemos esas oscilaciones cuando está en movimiento.
Para que veamos la importancia de la fuerza ejercida por el gripper: 


<img width="998" height="582" alt="imagen" src="https://github.com/user-attachments/assets/4daec799-0790-42d9-ad5b-1d76bff5c022" />

