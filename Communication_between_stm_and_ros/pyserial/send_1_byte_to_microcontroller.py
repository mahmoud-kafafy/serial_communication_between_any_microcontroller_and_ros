
import serial
import time

# Configure the serial port
SerialObj = serial.Serial('COM8')  # Change 'COM8' to match your device
SerialObj.baudrate = 115200           # Set Baud rate to 9600
SerialObj.bytesize = 8              # Number of data bits = 8
SerialObj.parity = 'N'              # No parity
SerialObj.stopbits = 1              # Number of Stop bits = 1

#time.sleep(1)  # Allow time for the Arduino to settle down

# Define the byte to send
speed = 43  # Example value for the byte

# Create a bytes object containing the byte to send
byte_to_send = bytes([speed])

# Write the byte to the serial port
BytesWritten = SerialObj.write(byte_to_send)

# Print the number of bytes written
print('BytesWritten = ', BytesWritten)

SerialObj.close()  # Close the serial port
