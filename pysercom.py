# PySerialCommunication Module. Imported in `main.py` as 'psc'
"""
Module to control LEDs and other components through Arduino. Used in `main.py`.
"""

import time
import serial


class Semafix:
    """Random name for the class."""

    def __init__(self, port):
        self.port = port
        self.arduino = serial.Serial(port, 9600)
        time.sleep(2)

    def green_ligth_line1(self):
        """Overwrites the status of an Arduino pin."""
        self.arduino.write(b"1")

    def gree_ligth_line2(self):
        """Overwrites the status of an Arduino pin."""
        self.arduino.write(b"2")
