import serial
import matplotlib.pyplot as plt
import time

# Configure the serial port
ser = serial.Serial('COM8', 115200)  # Change 'COM8' to match your device and baud rate

# Initialize lists to store data
received_values = []
timestamps = []

# Initialize start time
start_time = time.time()

# Plotting interval (in seconds)
plot_interval = 1.0  # Adjust this value as needed

try:
    while True:
        # Read four bytes from the serial port
        bytes_read = ser.read(4)
        
        # Check if four bytes are read
        if len(bytes_read) == 4:
            # Combine the bytes to form a uint32 number
            uint32_value = (bytes_read[0] << 24) | (bytes_read[1] << 16) | (bytes_read[2] << 8) | bytes_read[3]
            
            # Record the elapsed time since start
            elapsed_time = time.time() - start_time
            
            # Store the received value and timestamp
            received_values.append(uint32_value)
            timestamps.append(elapsed_time)
            
            # Check if it's time to update the plot
            if elapsed_time >= plot_interval:
                # Plot the data
                plt.plot(timestamps, received_values, color='b')
                plt.xlabel('Time (s)')
                plt.ylabel('Received Value')
                plt.title('Received Value over Time')
                plt.grid(True)
                plt.pause(0.05)  # Pause for a short time to update the plot
                
                # Reset lists for next interval
                received_values = []
                timestamps = []
                
                # Update start time
                start_time = time.time()
            
except KeyboardInterrupt:
    # Close the serial port when KeyboardInterrupt (Ctrl+C) is detected
    ser.close()
    print("Serial port closed")

# Show the plot
plt.show()
