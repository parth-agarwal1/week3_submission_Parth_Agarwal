#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from custom_message.msg import RoverStatus
from geometry_msgs.msg import Twist, Pose
from builtin_interfaces.msg import Duration


class RoverPublisher(Node):

    def __init__(self):
        super().__init__('rover_publisher')
        self.publisher_ = self.create_publisher(RoverStatus, 'rover_status', 10)
        self.timer = self.create_timer(2.0, self.publish_status)
        self.start_time = self.get_clock().now()
        
    def publish_status(self):
        #Example: Publishing an example custom message, no updating the duration yet.
        msg = RoverStatus()
        # Fill velocity (linear and angular)
        twist = Twist()
        twist.linear.x = 1.0
        twist.angular.z = 0.5
        msg.velocity = twist
        # Distance traveled
        msg.distance_travelled = 12.5
        # Coordinates
        pose = Pose()
        pose.position.x = 3.0
        pose.position.y = 1.5
        pose.position.z = 0.0
        msg.position = pose
        # Battery
        msg.battery_level = 78.3  # %
        # Time of travel
        duration = self.get_clock().now() - self.start_time
        msg.time_taken = Duration()
        msg.time_taken.sec = int(duration.nanoseconds // 1e9)
        msg.time_taken.nanosec = int(duration.nanoseconds % 1e9)
        self.publisher_.publish(msg)
        self.get_logger().info(
    f"\n--- Rover Status ---\n"
    f"Velocity:\n"
    f"  Linear:  x={msg.velocity.linear.x}, y={msg.velocity.linear.y}, z={msg.velocity.linear.z}\n"
    f"  Angular: x={msg.velocity.angular.x}, y={msg.velocity.angular.y}, z={msg.velocity.angular.z}\n"
    f"Distance Travelled: {msg.distance_travelled}\n"
    f"Position:\n"
    f"  x={msg.position.position.x}, y={msg.position.position.y}, z={msg.position.position.z}\n"
    f"Battery Level: {msg.battery_level}%\n"
    f"Time Travelled: {msg.time_taken.sec}s {msg.time_taken.nanosec}ns\n"
)


def main(args=None):
    rclpy.init(args=args)
    node = RoverPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
