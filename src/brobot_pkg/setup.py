from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'brobot_pkg' # package_name should equal the name of
# the python module not necessarily the ros2 package name. 
# When you initially do ros2 pkg create ros2 creates both the 
# ros2 package name(the outer brobot_pkg) and the python module
#  name(the inner brobot_pkg) but we can just rename the inner 
# brobot_pkg to be something else.

setup(
    name=package_name,
    version='0.0.0',

    packages=find_packages(
        include=[package_name, package_name + '.*']
    ),

    data_files=[
        # ros package index
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        # package.xml
        (
            'share/' + package_name,
            ['package.xml']
        ),

        # launch files
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),

        # gazebo worlds
        (
            os.path.join('share', package_name, 'worlds'),
            glob('worlds/*.sdf')
        ),

        # gazebo models
        (
            os.path.join(
                'share',
                package_name,
                'models',
                'brobot_car'
            ),
            glob('models/brobot_car/*')
        ),

        # bridge config
        (
            os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')
        ),
    ],

    install_requires=[
        'setuptools',
    ],

    zip_safe=True,

    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL@example.com',

    description='ROS 2 package for the Brobot mobile robot simulation.',

    license='Apache-2.0',

    entry_points={
        'console_scripts': [
            'keyboard_teleop = brobot_pkg.keyboard_teleop:main',
        ],
    },
)
