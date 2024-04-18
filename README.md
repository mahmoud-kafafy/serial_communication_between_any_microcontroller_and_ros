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

3. also you may need **usb to mini usb cable** that supports data transfer 

4. Connections:
<img src="https://iotforgeeks.com/wp-content/uploads/2020/03/Programming-STM32-with-USB-to-Serial-TTL.jpg" width="500" height="300">

## Steps of Configuration 

### Configuration on Microcontroller  
I use STM32F103C8T6
If you want to configure uart communication using stm32 boards you can watch this video: https://www.youtube.com/watch?v=dEQwSl8mCFs&t=788s
which help me in easy way how to configure uart from microcontroller by using generated driver stmcubemx
### Configuration on Python file which can run on (PC, Jetson or Raspberry Pi)
1- you need to install pyserial library if not by write in windows or Linux terminal
```
pip install pyserial
```
2- Open Visual Studio code and use the file you need from the repo you will find to read 1 byte and 2 bytes from uart and file to send data on uart and files to connect with ros to send and receive data

3- you must Configure the serial port to make uart communication you do this in python file 
  3.1 Change COM to match your device
 in windows by open device manager and know the number of port 
 in linux 
 ```
 sudo dmesg | tail
 ```
 <img src="https://www.xanthium.in/sites/default/files/inline-images/arduino-name-linux-dmesg.png" width="1500" height="300">
 
 for USB to serial Converters you will write like this in your code:
 
 ```
 SerialObj = serial.Serial('/dev/ttyACM0')
 ```
 
 3.2 Set Baud rate as you set in controller  
 3.3 Configure Number of data bits  
 3.4 Configure No parity  
 3.5 Configure Number of Stop bits = 1  

## Important Notes

You can't send more than 1 byte on uart but if you need to sent more than 1 byte you must make array of characters in your stm and in your python code as you can see in file send_2_bytes
 ```
 bytes_to_send = bytes([byte1, byte2, byte3])
 BytesWritten = SerialObj.write(bytes_to_send)
 ```
also you can put this line in your callback function in microcontroller to recieve array of chateachters 

 ```
 rx_buffer[rx_index++] = huart->Instance->DR;
 ```
after write this you cant receive the 3 bytes you sent in buffer 
 ```
rx_buffer[0]
rx_buffer[1]
rx_buffer[2]
 ```

