import serial

# Configure the serial port
ser = serial.Serial('COM5', 115200)  # Change 'COM8' to match your device and baud rate

try:
    while True:
        # Read one byte from the serial port
        byte_read = ser.read(1)
        
        # Check if a byte is read
        if byte_read:
            # Convert the byte to an integer using ord()
            int_value = ord(byte_read)
            
            # Process the integer value here
            print(int_value)
            
except KeyboardInterrupt: 
    # Close the serial port when KeyboardInterrupt (Ctrl+C) is detected
    ser.close()
    print("Serial port closed")
