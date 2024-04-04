import serial

# Configure the serial port
ser = serial.Serial('COM8', 115200)  # Change 'COM8' to match your device and baud rate

try:
    while True:
        # Read four bytes from the serial port
        bytes_read = ser.read(4)
        
        # Check if four bytes are read
        if len(bytes_read) == 4:
            # Combine the bytes to form a uint32 number
            uint32_value = (bytes_read[0] << 24) | (bytes_read[1] << 16) | (bytes_read[2] << 8) | bytes_read[3]
            
            # Process the uint32 value here
            print(uint32_value)
            
except KeyboardInterrupt:
    # Close the serial port when KeyboardInterrupt (Ctrl+C) is detected
    ser.close()
    print("Serial port closed")
