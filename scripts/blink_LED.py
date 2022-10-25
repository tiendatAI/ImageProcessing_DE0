"""
Send command blink LED via UART
"""

from __future__ import division, absolute_import, print_function

import sys
import glob
import time
import serial
import logging

#config for logging 
logging.basicConfig(format="%(asctime)s-%(levelname)s-%(message)s", level=logging.INFO)

def serial_ports() -> list:
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def open_com(port):
    try:
        ser = serial.Serial(
            port= port,
            baudrate=9600,
            timeout=0.1,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            xonxoff=False, 
            rtscts=False, 
            write_timeout=None, 
            dsrdtr=False,
            inter_byte_timeout=None, 
            exclusive=None
            )
        ser.isOpen() # try to open port, if possible print message and proceed with 'while True:'
        logging.info("Port is opened!")
    
    except IOError as error: # if port is already opened, close it and open it again and print message
        ser.close() # pyright: reportUnboundVariable=false
        ser.open()
        logging.info("Port was already open, was closed and opened again!")
    
    return ser

def sendLED_Data(ser, data=0, delay=0.001):
    cmd = b'\x0F'
    ser.write(cmd)
    time.sleep(delay)
    cmd = data.to_bytes(1, 'big')
    ser.write(cmd)
    time.sleep(delay)

def main():
    list_ports = serial_ports()
    ser = open_com(list_ports[0]) #first port
    
    while True:
        sendLED_Data(ser)     
        
        if 0xFF==ord('q'):
            break
    

if __name__ == '__main__':
    main()