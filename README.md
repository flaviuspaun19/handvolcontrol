# Gesture-Based Volume Control HMI 🔊

Project that explores touchless Human-Machine Interfaces (HMI). It uses an ultrasonic sensor to track hand distance and translate those movements into system volume commands on a PC. 

It's essentially a DIY version of the gesture controls found in modern automotive dashboards, bridging embedded hardware with OS-level software.

## 📺 Project Demo
You can find the full recording of the system working in the **`/Media`** folder. The video shows the real-time feedback on the LCD as the volume slider moves on the PC.

## 💻 Technical Stack
I moved away from the standard Arduino IDE for this project to use a more professional workflow:

- **Firmware**: Developed in **VS Code + PlatformIO** using C++. This allowed for better folder structure (`src/`, `include/`) and automated dependency management.
- **Hardware Documentation**: Designed a full schematic in **KiCad** to ensure signal integrity and proper power distribution, it can be found in **`/Hand_Sensor_HMI`**.
- **Host App**: A Python script using `pyserial` for data acquisition and `PyAutoGUI` for system-level volume control.

## 📐 Hardware Specifications
All logical connections were mapped in KiCad before assembly.
- **Microcontroller**: Arduino Uno R3
- **Display**: Displaytronic **LM16255K** 16x2 LCD (running in 4-bit parallel mode to conserve GPIOs)
- **Sensor**: HC-SR04 Ultrasonic Sensor (Trig: Pin 9, Echo: Pin 10)
- **Logic**: 4-bit data bus mapped to Arduino Pins D5-D2

## 🛠️ How to Setup
1. **Hardware**: Follow the schematic in the **`/Hand_Sensor_HMI`** folder. 
2. **Firmware**: Open the project in VS Code with the PlatformIO extension and click "Upload." It will automatically handle the `LiquidCrystal` library.
3. **Software**: Run `python src/volume_control.py` on your PC to start the serial bridge.

*Note: Make sure to adjust the potentiometer on your breadboard if the LCD text isn't visible on first boot!*
