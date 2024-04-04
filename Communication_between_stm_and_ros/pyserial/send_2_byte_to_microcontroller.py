# Python code transmits a byte 'A' to Arduino /Microcontroller to Blink LED
# Requires PySerial

# (c) www.xanthium.in 2022
# Rahul.S

# https://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial


import serial
import time

SerialObj = serial.Serial('COM5') # COMxx   format on Windows

                                   
                                   #/dev/ttyUSBx format on Linux
                                   #
                                   #Eg /dev/ttyUSB0
                                   #SerialObj = serial.Serial('/dev/ttyUSB0')

SerialObj.baudrate = 115200  # set Baud rate to 9600
SerialObj.bytesize = 8     # Number of data bits = 8
SerialObj.parity   ='N'    # No parity
SerialObj.stopbits = 1     # Number of Stop bits = 1

#Another way to configure the Ports
#SerialObj.bytesize = serial.EIGHTBITS     # Number of data bits = 8
#SerialObj.bytesize = serial.SEVENBITS     # Number of data bits = 7

#SerialObj.parity   = serial.PARITY_NONE   # No parity
#SerialObj.parity   = serial.PARITY_EVEN   # Parity Even

#SerialObj.stopbits = serial.STOPBITS_ONE  # Number of Stop bits = 1


#time.sleep(1)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.


# Define the bytes to send
speed = 20  # Example value for the first byte
byte2 = 0

if speed < 0:
    byte2 = 10  # Example value for the second byte
    speed = speed * -1 

bytes_to_send = bytes([speed, byte2])

# Write the bytes to the serial port
BytesWritten = SerialObj.write(bytes_to_send)

# Print the number of bytes written
print('BytesWritten = ', BytesWritten)
'''
for i in range(rangee):  # Change 'range' to a different variable name to avoid conflicts
    BytesWritten = SerialObj.write(bytes([x]))  # Convert 'x' to a bytes object before writing
    x += 1  # Increment 'x'

    print('BytesWritten = ', BytesWritten)
    time.sleep(1) 
'''
    

SerialObj.close()          # Close the port


