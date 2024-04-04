#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16

import serial


def publish_counts():
    # Initialize the ROS node
    rospy.init_node('count_publisher', anonymous=True)

    # Create a publisher for the "right_ticks" topic
    pub = rospy.Publisher('right_ticks', Int16, queue_size=10)
    pub2 = rospy.Publisher('left_ticks', Int16, queue_size=10)

    # Configure the serial port
    # Change 'COM8' to match your device and baud rate
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    oldcounts = 0

    try:
        while not rospy.is_shutdown():
            # Read three bytes from the serial port
            bytes_read = ser.read(2)

            # Check if three bytes are read
            if len(bytes_read) == 2:
                # Extract direction from the received bytes
                counts = bytes_read[0] | (bytes_read[1] << 8)
                # Convert to signed 16-bit integer
                #counts=counts-32768


                #if check > 65000:
                #   counts = -32768
                #   oldcounts = 0
              
                pub.publish(counts)
                pub2.publish(counts)
                print(counts)
                oldcounts = counts

    except KeyboardInterrupt:
        # Close the serial port when KeyboardInterrupt (Ctrl+C) is detected
        ser.close()
        print("Serial port closed")


if __name__ == '__main__':
    try:
        publish_counts()
    except rospy.ROSInterruptException:
        pass
