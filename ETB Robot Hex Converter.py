import serial
import time
import struct

while True:

    pw = int(input('Enter the decimal pulse in us :'))
    pw_ls = 2000 - pw
    pw_rs = 1000 + pw

    Pw_ls = pw_ls * 4
    Pw_rs = pw_rs * 4

    if (pw >= 0) and (pw <= 1000):

        # Setting up the variables
        set_target = 0x84     # default string for Maestro

        s1 = 0     # servo 1 string
        s2 = 1     # servo 2 string
        s3 = 2     # servo 3 stringb
        s4 = 3     # servo 4 string
        s5 = 4     # servo 5 string
        s6 = 5     # servo 6 string
        s7 = 6     # servo 7 string

        '''lsb = Pw & 0x7F
        msb = (Pw >> 7) & 0x7F
        lsb_hex = hex(lsb)  # converts least significant byte into hexadecimal
        msb_hex = hex(msb)  # converts most significant byte into hexadecimal
        print bin(lsb)
        print bin(msb)'''

        cmd_ls = (Pw_ls & 0x7F) + ((Pw_ls & 0x3F80) << 1)
        cmd_rs = (Pw_rs & 0x7F) + ((Pw_rs & 0x3F80) << 1)

        ser = serial.Serial('COM6')
        ser.write('\xAA')
        CMD1 = struct.pack('<BBH', set_target, s1, cmd_rs)
        CMD2 = struct.pack('<BBH', set_target, s2, cmd_ls)
        CMD3 = struct.pack('<BBH', set_target, s3, cmd_rs)
        CMD4 = struct.pack('<BBH', set_target, s4, cmd_rs)
        CMD5 = struct.pack('<BBH', set_target, s6, cmd_rs)
        CMD6 = struct.pack('<BBH', set_target, s7, cmd_rs)

        ser.write(CMD1)
        ser.write(CMD2)
        ser.write(CMD3)
        ser.write(CMD4)
        ser.write(CMD5)
        ser.write(CMD6)
        ser.close()
        #import pdb; pdb.set_trace()



    else:
        print 'Pulse Width should be 1000us - 2000us'
        continue

