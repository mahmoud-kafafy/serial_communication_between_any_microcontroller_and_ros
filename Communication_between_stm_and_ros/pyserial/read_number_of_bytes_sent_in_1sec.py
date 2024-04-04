import serial
import time

# Configure the serial port
ser = serial.Serial('COM8', 115200)  # Change 'COM8' to match your device and baud rate

try:
    byte_count = 0
    start_time = time.time()

    while True:
        # Read one byte from the serial port
        byte_read = ser.read()
        
        # Increment the byte count
        byte_count += 1
        
        # Get the current time in seconds since the epoch
        current_time_seconds = time.time()
        
        # Check if one second has elapsed
        if current_time_seconds - start_time >= 1:
            # Print the byte count for the previous second
            print(f"Bytes received in the last second: {byte_count}")
            
            # Reset the byte count and start time for the next second
            byte_count = 0
            start_time = time.time()
        
        # Check if byte is not empty
        if byte_read:
            # Convert byte to integer value
            byte_as_number = ord(byte_read)
            
            # Process the byte here
            print(f"{byte_as_number}", end=", ")
            
except KeyboardInterrupt:
    # Close the serial port when KeyboardInterrupt (Ctrl+C) is detected
    ser.close()
    print("\nSerial port closed")
