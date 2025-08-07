#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32



class Clock(Node):

    def __init__(self):
        super().__init__('clock')
        self.sec_pub = self.create_publisher(Int32, '/second', 10)
        self.min_pub = self.create_publisher(Int32, '/second', 10)
        self.hour_pub = self.create_publisher(Int32, '/second', 10)
        self.time_pub = self.create_publisher(String, '/clock', 10)
        self.create_publisher(Int32, '/second', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        
        self.sec = Int32()
        self.min = Int32()
        self.hr = Int32()
        
        #setting all data to zero
        self.sec.data = 0
        self.min.data = 0
        self.hr.data = 0
        
    def timer_callback(self):

        self.sec.data+=1
        
        #conditionals
        if (self.sec.data >= 60) :
            self.sec.data = 0
            self.min.data +=1
        
        if(self.min.data >= 60) :
            self.min.data = 0
            self.hr.data +=1
            
        self.sec_pub.publish(self.sec)
        self.min_pub.publish(self.min)
        self.hour_pub.publish(self.hr)
            
        time = String()
        time.data = f'{self.hr.data:02}:{self.min.data:02}:{self.sec.data:02}'    
        self.time_pub.publish(time)
        self.get_logger().info(f'Current_time: {time.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Clock()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
