
import serial

# Configure the serial port
ser = serial.Serial('COM9', 115200)  # Change 'COM8' to match your device and baud rate

try:
    while True:
        # Read three bytes from the serial port
        bytes_read = ser.read(2)
        
        # Check if three bytes are read
        if len(bytes_read) == 2:
            # Extract direction from the received bytes
            counts = bytes_read[0] | (bytes_read[1] << 8)

            #if bytes_read[2] > 5 :
                #counts = counts * -1
             #   counts=-65536+counts
            
            # Extract the third byte
            #third_byte = bytes_read[2]
            
            # Process direction and third_byte here
            print("counts:", counts)
            #print("Third Byte:", third_byte)
            
except KeyboardInterrupt:
    # Close the serial port when KeyboardInterrupt (Ctrl+C) is detected
    ser.close()
    print("Serial port closed")