import rclpy
from rclpy.node import Node

class CommandSubNode(Node):
    def __init__(self):
        super().__init__('command_sub_node')
        self.get_logger().info('Command node has subscribed..')