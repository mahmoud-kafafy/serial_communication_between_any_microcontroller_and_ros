import serial
import matplotlib.pyplot as plt
from datetime import datetime

# Configure the serial port
ser = serial.Serial('COM9', 115200)  # Change 'COM8' to match your device and baud rate

# Create a figure and axis for plotting
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line, = ax.plot([], [])  # Initialize an empty plot

# Set plot labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Real-time Plot')

# Add a red line at a constant y-value
constant_y_value = 70  # Adjust the y-value as needed
ax.axhline(y=constant_y_value, color='red', linestyle='--')

# Initialize an empty list for buffering received data
buffer_size = 100  # Adjust buffer size as needed
buffer = []

try:
    while True:
        # Read as many bytes as available from the serial port
        bytes_available = ser.in_waiting
        if bytes_available:
            bytes_read = ser.read(bytes_available)
            
            # Get the current time
            current_time = datetime.now()
            
            # Extend the buffer with tuples containing (time, value)
            buffer.extend([(current_time, byte) for byte in bytes_read])
            
            # If the buffer exceeds the desired size, update the plot and truncate the buffer
            if len(buffer) >= buffer_size:
                # Extract time and value from the buffer
                times = [data[0] for data in buffer]
                values = [data[1] for data in buffer]
                
                # Update the plot
                line.set_xdata(times)
                line.set_ydata(values)
                ax.relim()
                ax.autoscale_view()
                plt.draw()
                plt.pause(0.001)  # Adjust the pause duration as needed
                buffer = buffer[-buffer_size:]  # Keep the last 'buffer_size' elements of the buffer
            
except KeyboardInterrupt:
    # Close the serial port when KeyboardInterrupt (Ctrl+C) is detected
    ser.close()
    print("Serial port closed")
