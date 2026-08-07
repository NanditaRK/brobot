import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class KeyboardPublisherNode(Node):


    def __init__(self):
        super().__init__('keyboard_pub_node')
        self.get_logger().info('keyboard pub node has started')

        self.publisher = self.create_publisher(String, 'commands_topic', 5)

        self.timer = self.create_timer(1.0, self.publish_msg)

    def publish_msg(self):
        
        msg = String()

        msg.data = "Hello from ROS 2 node"

        self.publisher.publish(msg)

        self.get_logger().info(f"Published message: {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    node = KeyboardPublisherNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
