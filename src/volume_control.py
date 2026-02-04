import serial
import pyautogui
import time

# --- CONFIGURATION ---
# Check the bottom bar of VS Code/PlatformIO for your port (e.g., 'COM3')
arduino_port = 'COM5' 
baud_rate = 9600

print("Initializing Hand Sensor Controller...")

try:
    # Initialize serial connection
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    # Wait for Arduino to reset after serial connection
    time.sleep(2) 
    print(f"Successfully connected to {arduino_port}")
    print("Ready! Move hand: 2-12cm (UP), 12-25cm (DOWN)")
except Exception as e:
    print(f"ERROR: Could not connect to {arduino_port}.")
    print("Check if the Serial Monitor is open or if the port name is correct.")
    exit()

try:
    while True:
        if ser.in_waiting > 0:
            # Read line from Arduino, decode bytes to string, and strip whitespace
            command = ser.readline().decode('utf-8').strip()
            
            if command == "UP":
                print(">>> Action: Volume Up")
                pyautogui.press('volumeup') # Sends OS-level keyboard interrupt
            elif command == "DOWN":
                print(">>> Action: Volume Down")
                # `pyautogui` is a Python module that allows you to programmatically control the mouse
                # and keyboard to automate interactions with the GUI (Graphical User Interface) of the
                # operating system. In this specific code snippet, `pyautogui` is being used to
                # simulate pressing the volume up and volume down keys on the keyboard based on the
                # commands received from an Arduino device connected via serial communication.
                pyautogui.press('volumedown')
                
        time.sleep(0.01) # Small delay to prevent high CPU usage

except KeyboardInterrupt:
    print("\nStopping controller...")
    ser.close() # Cleanly close the serial port