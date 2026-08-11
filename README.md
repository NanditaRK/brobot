# Brobot

A project to mess around with ROS 2 and Gazebo simulations. 
Learned how to put together launch files and use the ros_gz_sim and ros_gz_bridge packages.
Also learned how plugins work with Gazebo.

## Commands to run =)

Make sure you have ROS 2 installed (I used Jazzy)

Source the ROS 2 install
```bash
source /opt/ros/jazzy/setup.bash
```

Create a ROS 2 workspace and package
```bash
mkdir ros2_ws
cd ros2_ws
```

Clone the repo
```bash
git clone https://github.com/NanditaRK/brobot.git
mv /brobot /brobot_pkg
```

Build the package
```bash
# build only brobot_pkg
colcon build --packages-select brobot_pkg

# build all packages
colcon build

# build with a symlink to install folder so that you dont have to rebuild everything when you only change python source code (only works for source code and python)
colcon build --packages-select brobot_pkg --symlink-install
```

Source the workspace
```bash
cd ~/ros2_ws
source install/setup.bash
```

Run the simulation
```bash
ros2 launch brobot_pkg simulation.launch.py
```

Run the keyboard teleop
```bash
ros2 run brobot_pkg keyboard_teleop
```
