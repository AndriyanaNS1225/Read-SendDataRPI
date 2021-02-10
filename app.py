from threading import Thread
import serial
import time
import connection
import serverhandle

baudrate = 115200
serial_timeout = 5 #in seconds
#check port with command "dmesg | grep tty", without quotation marks
telemetry_port = '/dev/ttyS0'
node5_port = '/dev/ttyUSB0'
timeInterval = 5 #in minutes

telemetry = serial.Serial(telemetry_port, baudrate=baudrate, timeout=serial_timeout)
node5 = serial.Serial(node5_port, baudrate=baudrate, timeout=serial_timeout)

if __name__ == '__main__':
    telemetry.close()
    telemetry.open()
    node5.close()
    node5.open()
    time.sleep(2)
    thread1 = Thread(target=connection.background_thread, args=(telemetry,node5,timeInterval))
    thread2 = Thread(target=serverhandle.background_comm, args=(timeInterval,))
    thread1.start()
    thread2.start()
