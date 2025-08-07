#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class S2Publisher(Node):
    def __init__(self):
        super().__init__('s2_publisher')
        self.subscription = self.create_subscription(String,'/s1', self.listener_callback,10)
        self.publisher_ = self.create_publisher(String, '/s2', 10)

    def listener_callback(self, msg):
        incoming_color = msg.data
        # Determine opposite color
        opposite_color = 'red' if (incoming_color == 'green') else 'green'
        out_msg = String()
        out_msg.data = opposite_color
        self.publisher_.publish(out_msg)
        self.get_logger().info(f'/s2: {opposite_color}')

def main(args=None):
    rclpy.init(args=args)
    node = S2Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
