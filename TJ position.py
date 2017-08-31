import ikpy
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import pi
import struct
import serial
import time


tj = ikpy.chain.Chain.from_urdf_file('C:/Users/MUSTAFA/Desktop/tjxml.XML')


ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')


while True:

    xcm = float(input('x coord [cm] = '))
    ycm = float(input('y coord [cm] = '))
    zcm = float(input('z coord [cm] = '))

    if xcm <= 20 and ycm <= 20 and zcm <= 20:

        a = tj.plot([0, 0, 0, 0, 0, 0, 0], ax)

        xm = xcm / 100
        ym = ycm / 100
        zm = zcm / 100

        b = tj.inverse_kinematics([
            [1, 0, 0, xm],
            [0, 1, 0, ym],
            [0, 0, 1, zm],
            [0, 0, 0, 1]
        ])

        base, shoulder, elbow_pitch, elbow_rot, wrist_pitch, wrist_rot = b[1:]

        servos = list()
        servos.append(int(round(6000 + (base * 2000))))
        servos.append(int(round(6000 - (shoulder * 2000))))
        servos.append(int(round(6000 + (shoulder * 2000))))
        servos.append(int(round(6000 + (elbow_pitch * 2000))))
        servos.append(int(round(6000 + (elbow_rot * 2000))))
        servos.append(int(round(6000 + (wrist_pitch * 2000))))
        servos.append(int(round(6000 + (wrist_rot * 2000))))

        for s, us in zip(range(7), servos):
            #ser = serial.Serial('COM6')
            cmd = (us & 0x7F) + ((us & 0x3F80) << 1)
            set_target = 0x84  # default string for Maestro
            CMD = struct.pack('<BBH', set_target, s, cmd)
            print CMD, us/4
            ser = serial.Serial('COM6')
            ser.write('\xAA')
            ser.write(CMD)
            ser.close()

        print servos
        print ('\n' * 1)
        print 'The angles from base to head are : ', b[1:]
        tj.plot(b, ax)
        matplotlib.pyplot.show()

    else:
        exit()