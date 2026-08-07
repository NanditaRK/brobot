from setuptools import find_packages, setup

package_name = 'brobot_pkg' # package_name should equal the name of
# the python module not necessarily the ros2 package name. 
# When you initially do ros2 pkg create ros2 creates both the 
# ros2 package name(the outer brobot_pkg) and the python module
#  name(the inner brobot_pkg) but we can just rename the inner 
# brobot_pkg to be something else.

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nrklinux',
    maintainer_email='nrklinux@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'keyboard_pub_node = brobot_pkg.keyboard_pub_node:main',
        ],
    },
)
