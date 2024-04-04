#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import serial

# Callback function to handle incoming Twist messages
def cmd_vel_callback(msg):
    global SerialObj
    # Define the bytes to send
        
    # Define the bytes to send
    speed = msg.linear.x  # Example value for the first byte
      # Print the number of bytes written
    speed = int(speed)
    print('BytesWritten = ', speed)
    byte2 = 0

    if speed < 0:
        byte2 = 10  # Example value for the second byte
        speed = speed * -1 

    bytes_to_send = bytes([speed, byte2])

    # Write the bytes to the serial port
    BytesWritten = SerialObj.write(bytes_to_send)

  
if __name__ == "__main__":
    try:
        # Initialize the ROS node
        rospy.init_node('motor_2')

        # Configure the serial port
        SerialObj = serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1)   #(sudo dmesg | tail)

        # Subscribe to the cmd_vel topic
        rospy.Subscriber('/cmdd_vel', Twist, cmd_vel_callback)

        # Spin ROS
        rospy.spin()

        # Close the serial port when the node is shutdown
        SerialObj.close()
    except rospy.ROSInterruptException:
        pass