import serial
import time

ser = serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

def send_command(cmd, wait=1):
        ser.write(cmd.encode('utf-8') + b'\r\n')
        time.sleep(wait)
        output = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')
        print (output)

if ser.is_open:
        print('Connected')

        send_command('\n')
        send_command('enable')
        send_command('conf t')
        send_command('ip domain name cisco')
        send_command('hostname Router2')
        send_command('crypto key generate rsa modulus 2048')
        send_command('username cisco1 secret cisco')
        send_command(' line vty 0 4')
        send_command('transport input ssh')
        send_command('login local')
        send_command('exit')
        send_command('ip ssh version 2')

        print('Config complete')
        ser.close()