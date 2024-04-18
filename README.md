# serial_communication_between_any_microcontroller_and_ros

## Motivation to do this
 I encountered a challenge in bridging high-level control with low-level control systems, particularly in integrating motors and sensors such as encoders and IMUs within the Robot Operating System (ROS) framework. To overcome this hurdle, I sought an alternative approach to connect these components, moving away from the conventional ROS serial communication protocol.

My solution involved leveraging the PySerial library, a Python package designed for facilitating serial communication. PySerial allows seamless communication over UART (Universal Asynchronous Receiver-Transmitter) channels, providing a versatile and efficient means of data exchange.

By configuring my microcontroller to transmit and receive data via UART, I established a robust communication channel. This enabled interoperability with a variety of high-level control devices, including laptops, Jetson devices, and Raspberry Pi units with low level controllers such as : arduino , stm , tiva c and c200 ... etc.

Through this approach, I aimed to simplify the integration process while ensuring efficiency and reliability within the serial communication domain. This GitHub repository serves as a comprehensive resource detailing the implementation and utilization of this novel communication method in robotics projects.
 
## Connections and Components
1. usb to ttl  
   [FTDI Board Switchable 3.3V or 5V](https://store.fut-electronics.com/products/ftdi-board-switchable-3-3-or-5v)

2. microcontroller support uart peripheral

3. also you may need **usb to mini usb cable** that support data transfer 

4. Connections:
<img src="https://iotforgeeks.com/wp-content/uploads/2020/03/Programming-STM32-with-USB-to-Serial-TTL.jpg" width="500" height="300">

## Steps of Configuration 

### Configuration on Microcontroller  

### Configuration on Python file which can run on (PC, Jetson or Raspberry Pi)
