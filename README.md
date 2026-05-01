# Practica-final---Modelado-y-simulaci-n-de-robots

## 1º Robot en rviz

El robot cuenta con dos cámaras , una delante y otra en la pinza que enfoca al cubo. Las TFs están orientadas tal que todos los giros de las articulaciones son en el eje z, y la base y el footprint en el robot cumplen con la orientación propiesta en el REP-103 (x forward y left z up), así como los optical frames de las cámaras (z forward x right y down), salvo en la del brazo, que está configurada para mirar hacia abajo.

Podemos ver las articulaciones, los frames, y las imágenes de ambas cámaras en la siguiente imagen:

<img width="1449" height="945" alt="imagen" src="https://github.com/user-attachments/assets/52f764d7-b1ae-4625-af9a-7dcd91b71610" />

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

O en el pdf: *frames_2026-04-26_19.00.35.pdf* dentro de la carpeta rover_description
