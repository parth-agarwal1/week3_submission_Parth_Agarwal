#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class S1Publisher(Node):
    def __init__(self):
        super().__init__('s1_publisher')
        self.publisher_ = self.create_publisher(String, '/s1', 10)
        self.color = 'green'
        self.timer = self.create_timer(10.0, self.publish_color)  # 10-second interval

    def publish_color(self):
        msg = String()
        msg.data = self.color
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing to /s1: "{msg.data}"')
        #Change colours
        self.color = 'red' if (self.color == 'green') else 'green'

def main(args=None):
    rclpy.init(args=args)
    node = S1Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
