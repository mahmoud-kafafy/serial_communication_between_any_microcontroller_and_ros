
import serial
import threading

# Define a function to read messages from the serial port
def read_serial(ser):
    while True:
        if ser.in_waiting > 0:
            message = ser.readline().decode().strip()  # Read a line from the serial port
            print("Received message:", message)

# Open the serial port
ser = serial.Serial('COM8', 9600)

# Create a thread to continuously read from the serial port
read_thread = threading.Thread(target=read_serial, args=(ser,))
read_thread.daemon = True  # Set the thread as a daemon so it will exit when the main thread exits
read_thread.start()

# Main program continues to execute...
while True:
    # Perform other tasks or simply sleep
    pass