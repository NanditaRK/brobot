import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node


def generate_launch_description():

    package_name = 'brobot_pkg'

    package_share = get_package_share_directory(
        package_name
    )

    # setting file paths

    world = os.path.join(
        package_share,
        'worlds',
        'car_world.sdf'
    )

    model = os.path.join(
        package_share,
        'models',
        'brobot_car',
        'model.sdf'
    )

    bridge_config = os.path.join(
        package_share,
        'config',
        'bridge.yaml'
    )


    # gazebo

    gazebo = IncludeLaunchDescription(

        PythonLaunchDescriptionSource(

            os.path.join(
                get_package_share_directory(
                    'ros_gz_sim'
                ),
                'launch',
                'gz_sim.launch.py'
            )

        ),

        launch_arguments={
            'gz_args': f'-r {world}'
        }.items()

    )


   # spawn the robot sdf

    spawn_robot = Node(

        package='ros_gz_sim',

        executable='create',

        arguments=[
            '-world',
            'car_world',

            '-file',
            model,

            '-name',
            'brobot_car',

            '-x',
            '0',

            '-y',
            '0',

            '-z',
            '0.45',
        ],

        output='screen'

    )


    # roz-gazebo bridge

    bridge = Node(

        package='ros_gz_bridge',

        executable='parameter_bridge',

        parameters=[
            {
                'config_file': bridge_config
            }
        ],

        output='screen'

    )




    return LaunchDescription([

        gazebo,

        spawn_robot,

        bridge,
    ])