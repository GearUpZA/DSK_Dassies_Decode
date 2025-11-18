# DSK Dassies Decode - FIRST LEGO League Robot Programs

This repository contains Python programs for the DSK Dassies FLL (FIRST LEGO League) robot using LEGO SPIKE Prime hardware and Pybricks firmware.

## Overview

The DSK Dassies team has developed multiple mission runs for FLL competition challenges. These programs control a robot built with LEGO SPIKE Prime components.

## Hardware Configuration

### Robot Setup
- **Hub**: LEGO SPIKE Prime Hub
- **Drive Motors**:
  - Left Motor (MT_1): Port F - Counterclockwise direction
  - Right Motor (motor_2): Port D - Clockwise direction
- **Attachment Motors**:
  - Attachment Motor 1 (Att_MTR): Port A - Clockwise direction
  - Attachment Motor 2 (Att_MTR_2): Port B - Clockwise direction
- **Drive Base Configuration**:
  - Wheel diameter: 86mm
  - Axle track (distance between wheels): 132mm
  - Gyro sensor enabled for accurate turns

### Orientation
- Hub top side: Z-axis
- Hub front side: X-axis
- Positive turns = Right
- Negative turns = Left

## Programs

### DSK_FLL_RUN7.py
The main competition run program featuring a complex sequence of movements and attachment operations:
- Initial 650mm straight movement
- Multiple turns and adjustments
- Attachment motor operations at various angles
- Strategic positioning for mission completion
- Return to base sequence

### Dsk_Fll_Run2.py
A focused mission run that includes:
- Forward movement to target area
- Repetitive attachment actions (4 cycles)
- Precise turning and positioning
- Designed for specific mission objectives

### mission_09_10.py
A mission-specific program handling missions 9 and 10:
- Initial positioning and navigation
- Variable speed control
- Multiple turn sequences
- Extended return movement to base

## Requirements

- LEGO SPIKE Prime Hub
- Pybricks firmware installed on the hub
- Python 3.x (for development)
- Pybricks library

## Installation

1. Install Pybricks firmware on your LEGO SPIKE Prime Hub following the [official Pybricks installation guide](https://pybricks.com/install/spike-prime/)
2. Clone this repository:
   ```bash
   git clone https://github.com/GearUpZA/DSK_Dassies_Decode.git
   ```
3. Open the Python files in Pybricks Code or your preferred IDE

## Usage

1. Connect your LEGO SPIKE Prime Hub to your computer
2. Open the desired program file (e.g., `DSK_FLL_RUN7.py`)
3. Upload and run the program on your hub
4. Place the robot at the starting position on the FLL mat
5. Press the hub button to execute the run

## Programming Notes

- All programs use gyro-assisted navigation for improved accuracy
- Distances are measured in millimeters (mm)
- Angles are measured in degrees (°)
- Motor speeds are in mm/s or degrees/s depending on the command
- `Stop.HOLD` maintains motor position after movement completion

## Team

**DSK Dassies** - Participating in FIRST LEGO League competitions

## License

This project is open source and available for educational purposes.

## Contributing

Contributions, suggestions, and improvements are welcome! Please feel free to submit issues or pull requests.

## Acknowledgments

- FIRST LEGO League for providing the competition framework
- Pybricks team for the excellent firmware and libraries
- GearUp South Africa for supporting STEM education
