import ikpy
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import pi
import struct
import serial
import time


tj = ikpy.chain.Chain.from_urdf_file('C:/Users/MUSTAFA/'
                                     'Desktop/tjxml.XML')


ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')
#bx = matplotlib.pyplot.figure().add_subplot(111, projection='3d')
thetas = list()


for theta in np.arange(0, 2*pi, 1):

    y = 0.1 * np.cos(theta)
    z = 0.1 * np.sin(theta)

    a = tj.inverse_kinematics([
        [1, 0, 0, 0.15],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])

    tj.plot(a, ax)

    Max = (4 * pi) / 9

    base,shoulder,elbow_pitch,elbow_rot,wrist_pitch,wrist_rot = a[1:]

    servos = list()
    servos.append(int(round(6000 + (base * 9 * 2000) / (4 * pi))))
    servos.append(int(round(6000 - (shoulder * 9 * 2000) / (4 * pi))))
    servos.append(int(round(6000 + (shoulder * 9 * 2000) / (4 * pi))))
    servos.append(int(round(6000 + (elbow_pitch * 9 * 2000) / (4 * pi))))
    servos.append(int(round(6000 + (elbow_rot * 9 * 2000) / (4 * pi))))
    servos.append(int(round(6000 + (wrist_pitch * 9 * 2000) / (4 * pi))))
    servos.append(int(round(6000 + (wrist_rot * 9 * 2000) / (4 * pi))))

    ser = serial.Serial('COM6')
    a = ser.write('\x93')
    ser.close()
    while True:

        CMDS = list()
        for s, us in zip(range(7), servos):
            ser = serial.Serial('COM6')
            cmd = (us & 0x7F) + ((us & 0x3F80) << 1)
            cmd_hex = hex(cmd)
            set_target = 0x84  # default string for Maestro
            CMD = struct.pack('<BBH', set_target, s, cmd)
            ser.write('\xAA')
            ser.read(a)
            ser.write(CMD)
            #CMDS.append(CMD)
            print CMD, us/4


            print ('\n' * 1)
            thetas.append(CMDS)
            #time.sleep(0.1)
            print ('\n' * 1)
            print 'The angles from base to head are : ', a[1:]
            #import pdb; pdb.set_trace()
            matplotlib.pyplot.show()


'''ser = serial.Serial('COM6')
acceleration_20 = 5
cmd_a20 = (acceleration_20 & 0x7F) + ((acceleration_20 & 0x3F80) << 1)
ser.write(cmd_a20)
ser.close()

for theta in thetas:
    for CMD in theta:
        ser = serial.Serial('COM6')
        ser.write('\xAA')
        ser.write(CMD)
        time.sleep(0.5)
        ser.close()'''







