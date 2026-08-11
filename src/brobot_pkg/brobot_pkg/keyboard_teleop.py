#!/usr/bin/env python3

import select
import sys
import termios
import tty

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class KeyboardTeleop(Node):

    def __init__(self):

        super().__init__('keyboard_teleop')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        # vehicle limits
        self.linear_speed = 1.0
        self.angular_speed = 1.5

        # current command
        self.linear = 0.0
        self.angular = 0.0

        # publish constantly at 20 Hz
        self.timer = self.create_timer(
            0.05,
            self.publish_command
        )

    def publish_command(self):

        msg = Twist()

        msg.linear.x = self.linear
        msg.angular.z = self.angular

        self.publisher.publish(msg)

    def stop(self):

        self.linear = 0.0
        self.angular = 0.0

        self.publish_command()


def get_key(timeout=0.1):

    """
    read one key at a time without blocking the ROS node.
    """

    settings = termios.tcgetattr(sys.stdin)

    tty.setraw(sys.stdin.fileno())

    try:

        readable, _, _ = select.select(
            [sys.stdin],
            [],
            [],
            timeout
        )

        if not readable:
            return ''

        key = sys.stdin.read(1)

        # arrow keys (doesnt seem to work right now)

        if key == '\x1b':

            if select.select(
                [sys.stdin],
                [],
                [],
                0.01
            )[0]:

                key += sys.stdin.read(1)

            if select.select(
                [sys.stdin],
                [],
                [],
                0.01
            )[0]:

                key += sys.stdin.read(1)

            if key == '\x1b[A':
                return 'UP'

            if key == '\x1b[B':
                return 'DOWN'

            if key == '\x1b[C':
                return 'RIGHT'

            if key == '\x1b[D':
                return 'LEFT'

        return key

    finally:

        termios.tcsetattr(
            sys.stdin,
            termios.TCSADRAIN,
            settings
        )


def print_instructions():

    
    print('BROBOT KEYBOARD CONTROL')
    print('Use W, A, S, D to move forward, right, backwards, and left respectively.')
    print('Press space to stop.')
    print('Press q to quit.')



def main(args=None):

    rclpy.init(args=args)

    node = KeyboardTeleop()

    print_instructions()

    try:

        while rclpy.ok():

            key = get_key(0.05)

            if key in ('UP', 'w', 'W'):

                node.linear = node.linear_speed
                node.angular = 0.0

            elif key in ('DOWN', 's', 'S'):

                node.linear = -node.linear_speed
                node.angular = 0.0

            elif key in ('LEFT', 'a', 'A'):

                node.linear = 0.0
                node.angular = node.angular_speed

            elif key in ('RIGHT', 'd', 'D'):

                node.linear = 0.0
                node.angular = -node.angular_speed

            elif key == ' ':

                node.stop()

            elif key in ('q', 'Q'):

                node.stop()
                break

            rclpy.spin_once(
                node,
                timeout_sec=0.0
            )

    except KeyboardInterrupt:

        pass

    finally:

        node.stop()

        node.destroy_node()

        rclpy.shutdown()


if __name__ == '__main__':
    main()