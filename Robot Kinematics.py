import struct
import serial
import time



a = 1000 * 4
b = 1500 * 4
c = 2000 * 4

set_target = 0x84     # default string for Maestro
set_speed = 0x87      # default string for speed on Maestro
set_acceleration = 0x89     # default string for acceleration on Maestro


s1 = 0     # servo 1 string
s2 = 1     # servo 2 string
s3 = 2     # servo 3 string
s4 = 3     # servo 4 string
s5 = 4     # servo 5 string
s6 = 5     # servo 6 string
s7 = 6     # servo 7 string

cmd1 = (a & 0x7F) + ((a & 0x3F80) << 1)
cmd2 = (b & 0x7F) + ((b & 0x3F80) << 1)
cmd3 = (c & 0x7F) + ((c & 0x3F80) << 1)

speed_20 = 52       # 20% speed
speed_50 = 128      # 50% speed
speed_80 = 204      # 80% speed

cmd_s20 = (speed_20 & 0x7F) + ((speed_20 & 0x3F80) << 1)
cmd_s50 = (speed_50 & 0x7F) + ((speed_50 & 0x3F80) << 1)
cmd_s80 = (speed_80 & 0x7F) + ((speed_80 & 0x3F80) << 1)


acceleration_20 = 5       # 20% acceleration
acceleration_50 = 20      # 50% acceleration
acceleration_100 = 0        # unlimited acceleration

cmd_a20 = (acceleration_20 & 0x7F) + ((acceleration_20 & 0x3F80) << 1)
cmd_a50 = (acceleration_50 & 0x7F) + ((acceleration_50 & 0x3F80) << 1)
cmd_a100 = (acceleration_100 & 0x7F) + ((acceleration_100 & 0x3F80) << 1)


acceleration = raw_input('Please enter the desired acceleration 20%, 50% or 100% :')

while True:

    if acceleration == '20':

        while True:

            ser = serial.Serial('COM6')
            CMDA_20s1 = struct.pack('<BBH', set_acceleration, s1, cmd_a20)
            CMDA_20s2 = struct.pack('<BBH', set_acceleration, s2, cmd_a20)
            CMDA_20s3 = struct.pack('<BBH', set_acceleration, s3, cmd_a20)
            CMDA_20s4 = struct.pack('<BBH', set_acceleration, s4, cmd_a20)
            CMDA_20s5 = struct.pack('<BBH', set_acceleration, s5, cmd_a20)
            CMDA_20s6 = struct.pack('<BBH', set_acceleration, s6, cmd_a20)
            CMDA_20s7 = struct.pack('<BBH', set_acceleration, s7, cmd_a20)

            ser.write(CMDA_20s1)
            ser.write(CMDA_20s2)
            ser.write(CMDA_20s3)
            ser.write(CMDA_20s4)
            ser.write(CMDA_20s5)
            ser.write(CMDA_20s6)
            ser.write(CMDA_20s7)
            ser.close()

            print "1 - base yaw"
            print "2 - shoulder pitch"
            print "3 - elbow pitch"
            print "4 - elbow rotation"
            print "5 - wrist pitch"
            print "6 - wrist rotation"
            x = raw_input('Select a joint to test (1 - 6) :')

            if x == '1':

                speed = raw_input("Please enter desired speed 20%, 50% or 80% :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDBS1 = struct.pack('<BBH', set_speed, s1, cmd_s20)
                    ser.write(CMDBS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                        ser.write(CMDB1)
                        time.sleep(1.5)
                        CMDB3 = struct.pack('<BBH', set_target, s1, cmd3)
                        ser.write(CMDB3)
                        time.sleep(1.5)
                        ser.close()
                    ser = serial.Serial('COM6')
                    CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                    ser.write(CMDB1)
                    ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDBS2 = struct.pack('<BBH', set_speed, s1, cmd_s50)
                    ser.write(CMDBS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:

                        ser = serial.Serial('COM6')
                        CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                        ser.write(CMDB1)
                        time.sleep(1.4)
                        CMDB3 = struct.pack('<BBH', set_target, s1, cmd3)
                        ser.write(CMDB3)
                        time.sleep(1.4)
                        ser.close()
                    ser = serial.Serial('COM6')
                    CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                    ser.write(CMDB1)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDBS3 = struct.pack('<BBH', set_speed, s1, cmd_s80)
                    ser.write(CMDBS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                        ser.write(CMDB1)
                        time.sleep(1.3)
                        CMDB3 = struct.pack('<BBH', set_target, s1, cmd3)
                        ser.write(CMDB3)
                        time.sleep(1.3)
                        ser.close()
                    ser = serial.Serial('COM6')
                    CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                    ser.write(CMDB1)
                    ser.close()


            elif x == '2':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDLSS1 = struct.pack('<BBH', set_speed, s2, cmd_s20)
                    CMDRSS1 = struct.pack('<BBH', set_speed, s3, cmd_s20)
                    ser.write(CMDLSS1)
                    ser.write(CMDRSS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDLS1 = struct.pack('<BBH', set_target, s2, cmd3)
                        CMDRS1 = struct.pack('<BBH', set_target, s3, cmd1)
                        ser.write(CMDLS1)
                        ser.write(CMDRS1)
                        time.sleep(1.5)
                        CMDLS3 = struct.pack('<BBH', set_target, s2, cmd1)
                        CMDRS3 = struct.pack('<BBH', set_target, s3, cmd3)
                        ser.write(CMDLS3)
                        ser.write(CMDRS3)
                        time.sleep(1.5)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDLS2 = struct.pack('<BBH', set_target, s2, cmd2)
                    CMDRS2 = struct.pack('<BBH', set_target, s3, cmd2)
                    ser.write(CMDLS2)
                    ser.write(CMDRS2)
                    ser.close()


                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDLSS2 = struct.pack('<BBH', set_speed, s2, cmd_s50)
                    CMDRSS2 = struct.pack('<BBH', set_speed, s3, cmd_s50)
                    ser.write(CMDLSS2)
                    ser.write(CMDRSS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDLS1 = struct.pack('<BBH', set_target, s2, cmd3)
                        CMDRS1 = struct.pack('<BBH', set_target, s3, cmd1)
                        ser.write(CMDLS1)
                        ser.write(CMDRS1)
                        time.sleep(1.3)
                        CMDLS3 = struct.pack('<BBH', set_target, s2, cmd1)
                        CMDRS3 = struct.pack('<BBH', set_target, s3, cmd3)
                        ser.write(CMDLS3)
                        ser.write(CMDRS3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDLS2 = struct.pack('<BBH', set_target, s2, cmd2)
                    CMDRS2 = struct.pack('<BBH', set_target, s3, cmd2)
                    ser.write(CMDLS2)
                    ser.write(CMDRS2)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDLSS3 = struct.pack('<BBH', set_speed, s2, cmd_s80)
                    CMDRSS3 = struct.pack('<BBH', set_speed, s3, cmd_s80)
                    ser.write(CMDLSS3)
                    ser.write(CMDRSS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDLS1 = struct.pack('<BBH', set_target, s2, cmd3)
                        CMDRS1 = struct.pack('<BBH', set_target, s3, cmd1)
                        ser.write(CMDLS1)
                        ser.write(CMDRS1)
                        time.sleep(1.2)
                        CMDLS3 = struct.pack('<BBH', set_target, s2, cmd1)
                        CMDRS3 = struct.pack('<BBH', set_target, s3, cmd3)
                        ser.write(CMDLS3)
                        ser.write(CMDRS3)
                        time.sleep(1.2)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDLS2 = struct.pack('<BBH', set_target, s2, cmd2)
                    CMDRS2 = struct.pack('<BBH', set_target, s3, cmd2)
                    ser.write(CMDLS2)
                    ser.write(CMDRS2)
                    ser.close()

            elif x == '3':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDES1 = struct.pack('<BBH', set_speed, s4, cmd_s20)
                    ser.write(CMDES1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s4, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.5)
                        CMDE3 = struct.pack('<BBH', set_target, s4, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.5)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s4, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDES2 = struct.pack('<BBH', set_speed, s4, cmd_s50)
                    ser.write(CMDES2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s4, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.3)
                        CMDE3 = struct.pack('<BBH', set_target, s4, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s4, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDES3 = struct.pack('<BBH', set_speed, s4, cmd_s80)
                    ser.write(CMDES3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s4, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.3)
                        CMDE3 = struct.pack('<BBH', set_target, s4, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s4, cmd2)
                    ser.write(CMDE2)
                    ser.close()

            elif x == '4':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDES1 = struct.pack('<BBH', set_speed, s5, cmd_s20)
                    ser.write(CMDES1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s5, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.5)
                        CMDE3 = struct.pack('<BBH', set_target, s5, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.5)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s5, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDES2 = struct.pack('<BBH', set_speed, s5, cmd_s50)
                    ser.write(CMDES2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s5, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.3)
                        CMDE3 = struct.pack('<BBH', set_target, s5, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s5, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDES3 = struct.pack('<BBH', set_speed, s5, cmd_s80)
                    ser.write(CMDES3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s5, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.2)
                        CMDE3 = struct.pack('<BBH', set_target, s5, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.2)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s5, cmd2)
                    ser.write(CMDE2)
                    ser.close()

            elif x == '5':

                speed = raw_input('Please enter desired speed % :')

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDWPS1 = struct.pack('<BBH', set_speed, s6, cmd_s20)
                    ser.write(CMDWPS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:

                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWP1 = struct.pack('<BBH', set_target, s6, cmd1)
                        ser.write(CMDWP1)
                        time.sleep(1.5)
                        CMDWP3 = struct.pack('<BBH', set_target, s6, cmd3)
                        ser.write(CMDWP3)
                        time.sleep(1.5)
                        ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDWPS2 = struct.pack('<BBH', set_speed, s6, cmd_s50)
                    ser.write(CMDWPS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWP1 = struct.pack('<BBH', set_target, s6, cmd1)
                        ser.write(CMDWP1)
                        time.sleep(1.3)
                        CMDWP3 = struct.pack('<BBH', set_target, s6, cmd3)
                        ser.write(CMDWP3)
                        time.sleep(1.3)
                        ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDWPS3 = struct.pack('<BBH', set_speed, s6, cmd_s80)
                    ser.write(CMDWPS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWP1 = struct.pack('<BBH', set_target, s6, cmd1)
                        ser.write(CMDWP1)
                        time.sleep(1.2)
                        CMDWP3 = struct.pack('<BBH', set_target, s6, cmd3)
                        ser.write(CMDWP3)
                        time.sleep(1.2)
                        ser.close()

            elif x == '6':

                speed = raw_input("Please enter desired speed % : ")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDWRS1 = struct.pack('<BBH', set_speed, s7, cmd_s20)
                    ser.write(CMDWRS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWR1 = struct.pack('<BBH', set_target, s7, cmd1)
                        ser.write(CMDWR1)
                        time.sleep(1.0)
                        CMDWR3 = struct.pack('<BBH', set_target, s7, cmd3)
                        ser.write(CMDWR3)
                        time.sleep(1.0)
                        ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDWRS2 = struct.pack('<BBH', set_speed, s7, cmd_s50)
                    ser.write(CMDWRS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWR1 = struct.pack('<BBH', set_target, s7, cmd1)
                        ser.write(CMDWR1)
                        time.sleep(0.6)
                        CMDWR3 = struct.pack('<BBH', set_target, s7, cmd3)
                        ser.write(CMDWR3)
                        time.sleep(0.6)
                        ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDWRS3 = struct.pack('<BBH', set_speed, s7, cmd_s80)
                    ser.write(CMDWRS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWR1 = struct.pack('<BBH', set_target, s7, cmd1)
                        ser.write(CMDWR1)
                        time.sleep(0.35)
                        CMDWR3 = struct.pack('<BBH', set_target, s7, cmd3)
                        ser.write(CMDWR3)
                        time.sleep(0.35)
                        ser.close()

    elif acceleration == '50':

        while True:

            ser = serial.Serial('COM6')
            CMDA_50s1 = struct.pack('<BBH', set_acceleration, s1, cmd_a50)
            CMDA_50s2 = struct.pack('<BBH', set_acceleration, s2, cmd_a50)
            CMDA_50s3 = struct.pack('<BBH', set_acceleration, s3, cmd_a50)
            CMDA_50s4 = struct.pack('<BBH', set_acceleration, s4, cmd_a50)
            CMDA_50s5 = struct.pack('<BBH', set_acceleration, s5, cmd_a50)
            CMDA_50s6 = struct.pack('<BBH', set_acceleration, s6, cmd_a50)
            CMDA_50s7 = struct.pack('<BBH', set_acceleration, s7, cmd_a50)

            ser.write(CMDA_50s1)
            ser.write(CMDA_50s2)
            ser.write(CMDA_50s3)
            ser.write(CMDA_50s4)
            ser.write(CMDA_50s5)
            ser.write(CMDA_50s6)
            ser.write(CMDA_50s7)
            ser.close()

            print "1 - base yaw"
            print "2 - shoulder pitch"
            print "3 - elbow pitch"
            print "4 - elbow rotation"
            print "5 - wrist pitch"
            print "6 - wrist rotation"
            x = raw_input('Select a joint to test (1 - 6) :')

            if x == '1':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDBS1 = struct.pack('<BBH', set_speed, s1, cmd_s20)
                    ser.write(CMDBS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                        ser.write(CMDB1)
                        time.sleep(1.5)
                        CMDB3 = struct.pack('<BBH', set_target, s1, cmd3)
                        ser.write(CMDB3)
                        time.sleep(1.5)
                        ser.close()
                    ser = serial.Serial('COM6')
                    CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                    ser.write(CMDB1)
                    ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDBS2 = struct.pack('<BBH', set_speed, s1, cmd_s50)
                    ser.write(CMDBS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                        ser.write(CMDB1)
                        time.sleep(1.4)
                        CMDB3 = struct.pack('<BBH', set_target, s1, cmd3)
                        ser.write(CMDB3)
                        time.sleep(1.4)
                        ser.close()
                    ser = serial.Serial('COM6')
                    CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                    ser.write(CMDB1)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDBS3 = struct.pack('<BBH', set_speed, s1, cmd_s80)
                    ser.write(CMDBS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                        ser.write(CMDB1)
                        time.sleep(1.3)
                        CMDB3 = struct.pack('<BBH', set_target, s1, cmd3)
                        ser.write(CMDB3)
                        time.sleep(1.3)
                        ser.close()
                    ser = serial.Serial('COM6')
                    CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                    ser.write(CMDB1)
                    ser.close()


            elif x == '2':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDLSS1 = struct.pack('<BBH', set_speed, s2, cmd_s20)
                    CMDRSS1 = struct.pack('<BBH', set_speed, s3, cmd_s20)
                    ser.write(CMDLSS1)
                    ser.write(CMDRSS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDLS1 = struct.pack('<BBH', set_target, s2, cmd3)
                        CMDRS1 = struct.pack('<BBH', set_target, s3, cmd1)
                        ser.write(CMDLS1)
                        ser.write(CMDRS1)
                        time.sleep(1.5)
                        CMDLS3 = struct.pack('<BBH', set_target, s2, cmd1)
                        CMDRS3 = struct.pack('<BBH', set_target, s3, cmd3)
                        ser.write(CMDLS3)
                        ser.write(CMDRS3)
                        time.sleep(1.5)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDLS2 = struct.pack('<BBH', set_target, s2, cmd2)
                    CMDRS2 = struct.pack('<BBH', set_target, s3, cmd2)
                    ser.write(CMDLS2)
                    ser.write(CMDRS2)
                    ser.close()


                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDLSS2 = struct.pack('<BBH', set_speed, s2, cmd_s50)
                    CMDRSS2 = struct.pack('<BBH', set_speed, s3, cmd_s50)
                    ser.write(CMDLSS2)
                    ser.write(CMDRSS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDLS1 = struct.pack('<BBH', set_target, s2, cmd3)
                        CMDRS1 = struct.pack('<BBH', set_target, s3, cmd1)
                        ser.write(CMDLS1)
                        ser.write(CMDRS1)
                        time.sleep(1.3)
                        CMDLS3 = struct.pack('<BBH', set_target, s2, cmd1)
                        CMDRS3 = struct.pack('<BBH', set_target, s3, cmd3)
                        ser.write(CMDLS3)
                        ser.write(CMDRS3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDLS2 = struct.pack('<BBH', set_target, s2, cmd2)
                    CMDRS2 = struct.pack('<BBH', set_target, s3, cmd2)
                    ser.write(CMDLS2)
                    ser.write(CMDRS2)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDLSS3 = struct.pack('<BBH', set_speed, s2, cmd_s80)
                    CMDRSS3 = struct.pack('<BBH', set_speed, s3, cmd_s80)
                    ser.write(CMDLSS3)
                    ser.write(CMDRSS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDLS1 = struct.pack('<BBH', set_target, s2, cmd3)
                        CMDRS1 = struct.pack('<BBH', set_target, s3, cmd1)
                        ser.write(CMDLS1)
                        ser.write(CMDRS1)
                        time.sleep(1.2)
                        CMDLS3 = struct.pack('<BBH', set_target, s2, cmd1)
                        CMDRS3 = struct.pack('<BBH', set_target, s3, cmd3)
                        ser.write(CMDLS3)
                        ser.write(CMDRS3)
                        time.sleep(1.2)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDLS2 = struct.pack('<BBH', set_target, s2, cmd2)
                    CMDRS2 = struct.pack('<BBH', set_target, s3, cmd2)
                    ser.write(CMDLS2)
                    ser.write(CMDRS2)
                    ser.close()

            elif x == '3':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDES1 = struct.pack('<BBH', set_speed, s4, cmd_s20)
                    ser.write(CMDES1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s4, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.5)
                        CMDE3 = struct.pack('<BBH', set_target, s4, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.5)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s4, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDES2 = struct.pack('<BBH', set_speed, s4, cmd_s50)
                    ser.write(CMDES2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s4, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.3)
                        CMDE3 = struct.pack('<BBH', set_target, s4, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s4, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDES3 = struct.pack('<BBH', set_speed, s4, cmd_s80)
                    ser.write(CMDES3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s4, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.3)
                        CMDE3 = struct.pack('<BBH', set_target, s4, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s4, cmd2)
                    ser.write(CMDE2)
                    ser.close()

            elif x == '4':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDES1 = struct.pack('<BBH', set_speed, s5, cmd_s20)
                    ser.write(CMDES1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s5, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.5)
                        CMDE3 = struct.pack('<BBH', set_target, s5, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.5)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s5, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDES2 = struct.pack('<BBH', set_speed, s5, cmd_s50)
                    ser.write(CMDES2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s5, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.3)
                        CMDE3 = struct.pack('<BBH', set_target, s5, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s5, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDES3 = struct.pack('<BBH', set_speed, s5, cmd_s80)
                    ser.write(CMDES3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s5, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.2)
                        CMDE3 = struct.pack('<BBH', set_target, s5, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.2)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s5, cmd2)
                    ser.write(CMDE2)
                    ser.close()

            elif x == '5':

                speed = raw_input('Please enter desired speed % :')

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDWPS1 = struct.pack('<BBH', set_speed, s6, cmd_s20)
                    ser.write(CMDWPS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWP1 = struct.pack('<BBH', set_target, s6, cmd1)
                        ser.write(CMDWP1)
                        time.sleep(1.5)
                        CMDWP3 = struct.pack('<BBH', set_target, s6, cmd3)
                        ser.write(CMDWP3)
                        time.sleep(1.5)
                        ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDWPS2 = struct.pack('<BBH', set_speed, s6, cmd_s50)
                    ser.write(CMDWPS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWP1 = struct.pack('<BBH', set_target, s6, cmd1)
                        ser.write(CMDWP1)
                        time.sleep(1.3)
                        CMDWP3 = struct.pack('<BBH', set_target, s6, cmd3)
                        ser.write(CMDWP3)
                        time.sleep(1.3)
                        ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDWPS3 = struct.pack('<BBH', set_speed, s6, cmd_s80)
                    ser.write(CMDWPS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWP1 = struct.pack('<BBH', set_target, s6, cmd1)
                        ser.write(CMDWP1)
                        time.sleep(1.2)
                        CMDWP3 = struct.pack('<BBH', set_target, s6, cmd3)
                        ser.write(CMDWP3)
                        time.sleep(1.2)
                        ser.close()

            elif x == '6':

                speed = raw_input("Please enter desired speed % : ")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDWRS1 = struct.pack('<BBH', set_speed, s7, cmd_s20)
                    ser.write(CMDWRS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWR1 = struct.pack('<BBH', set_target, s7, cmd1)
                        ser.write(CMDWR1)
                        time.sleep(1.0)
                        CMDWR3 = struct.pack('<BBH', set_target, s7, cmd3)
                        ser.write(CMDWR3)
                        time.sleep(1.0)
                        ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDWRS2 = struct.pack('<BBH', set_speed, s7, cmd_s50)
                    ser.write(CMDWRS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWR1 = struct.pack('<BBH', set_target, s7, cmd1)
                        ser.write(CMDWR1)
                        time.sleep(0.6)
                        CMDWR3 = struct.pack('<BBH', set_target, s7, cmd3)
                        ser.write(CMDWR3)
                        time.sleep(0.6)
                        ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDWRS3 = struct.pack('<BBH', set_speed, s7, cmd_s80)
                    ser.write(CMDWRS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWR1 = struct.pack('<BBH', set_target, s7, cmd1)
                        ser.write(CMDWR1)
                        time.sleep(0.35)
                        CMDWR3 = struct.pack('<BBH', set_target, s7, cmd3)
                        ser.write(CMDWR3)
                        time.sleep(0.35)
                        ser.close()

    elif acceleration == '100':

        while True:

            ser = serial.Serial('COM6')
            CMDA_100s1 = struct.pack('<BBH', set_acceleration, s1, cmd_a100)
            CMDA_100s2 = struct.pack('<BBH', set_acceleration, s2, cmd_a100)
            CMDA_100s3 = struct.pack('<BBH', set_acceleration, s3, cmd_a100)
            CMDA_100s4 = struct.pack('<BBH', set_acceleration, s4, cmd_a100)
            CMDA_100s5 = struct.pack('<BBH', set_acceleration, s5, cmd_a100)
            CMDA_100s6 = struct.pack('<BBH', set_acceleration, s6, cmd_a100)
            CMDA_100s7 = struct.pack('<BBH', set_acceleration, s7, cmd_a100)

            ser.write(CMDA_100s1)
            ser.write(CMDA_100s2)
            ser.write(CMDA_100s3)
            ser.write(CMDA_100s4)
            ser.write(CMDA_100s5)
            ser.write(CMDA_100s6)
            ser.write(CMDA_100s7)
            ser.close()

            print "1 - base yaw"
            print "2 - shoulder pitch"
            print "3 - elbow pitch"
            print "4 - elbow rotation"
            print "5 - wrist pitch"
            print "6 - wrist rotation"
            x = raw_input('Select a joint to test (1 - 6) :')

            if x == '1':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDBS1 = struct.pack('<BBH', set_speed, s1, cmd_s20)
                    ser.write(CMDBS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                        ser.write(CMDB1)
                        time.sleep(1.5)
                        CMDB3 = struct.pack('<BBH', set_target, s1, cmd3)
                        ser.write(CMDB3)
                        time.sleep(1.5)
                        ser.close()
                    ser = serial.Serial('COM6')
                    CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                    ser.write(CMDB1)
                    ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDBS2 = struct.pack('<BBH', set_speed, s1, cmd_s50)
                    ser.write(CMDBS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                        ser.write(CMDB1)
                        time.sleep(1.4)
                        CMDB3 = struct.pack('<BBH', set_target, s1, cmd3)
                        ser.write(CMDB3)
                        time.sleep(1.4)
                        ser.close()
                    ser = serial.Serial('COM6')
                    CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                    ser.write(CMDB1)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDBS3 = struct.pack('<BBH', set_speed, s1, cmd_s80)
                    ser.write(CMDBS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                        ser.write(CMDB1)
                        time.sleep(1.3)
                        CMDB3 = struct.pack('<BBH', set_target, s1, cmd3)
                        ser.write(CMDB3)
                        time.sleep(1.3)
                        ser.close()
                    ser = serial.Serial('COM6')
                    CMDB1 = struct.pack('<BBH', set_target, s1, cmd1)
                    ser.write(CMDB1)
                    ser.close()


            elif x == '2':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDLSS1 = struct.pack('<BBH', set_speed, s2, cmd_s20)
                    CMDRSS1 = struct.pack('<BBH', set_speed, s3, cmd_s20)
                    ser.write(CMDLSS1)
                    ser.write(CMDRSS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDLS1 = struct.pack('<BBH', set_target, s2, cmd3)
                        CMDRS1 = struct.pack('<BBH', set_target, s3, cmd1)
                        ser.write(CMDLS1)
                        ser.write(CMDRS1)
                        time.sleep(1.5)
                        CMDLS3 = struct.pack('<BBH', set_target, s2, cmd1)
                        CMDRS3 = struct.pack('<BBH', set_target, s3, cmd3)
                        ser.write(CMDLS3)
                        ser.write(CMDRS3)
                        time.sleep(1.5)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDLS2 = struct.pack('<BBH', set_target, s2, cmd2)
                    CMDRS2 = struct.pack('<BBH', set_target, s3, cmd2)
                    ser.write(CMDLS2)
                    ser.write(CMDRS2)
                    ser.close()


                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDLSS2 = struct.pack('<BBH', set_speed, s2, cmd_s50)
                    CMDRSS2 = struct.pack('<BBH', set_speed, s3, cmd_s50)
                    ser.write(CMDLSS2)
                    ser.write(CMDRSS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDLS1 = struct.pack('<BBH', set_target, s2, cmd3)
                        CMDRS1 = struct.pack('<BBH', set_target, s3, cmd1)
                        ser.write(CMDLS1)
                        ser.write(CMDRS1)
                        time.sleep(1.3)
                        CMDLS3 = struct.pack('<BBH', set_target, s2, cmd1)
                        CMDRS3 = struct.pack('<BBH', set_target, s3, cmd3)
                        ser.write(CMDLS3)
                        ser.write(CMDRS3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDLS2 = struct.pack('<BBH', set_target, s2, cmd2)
                    CMDRS2 = struct.pack('<BBH', set_target, s3, cmd2)
                    ser.write(CMDLS2)
                    ser.write(CMDRS2)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDLSS3 = struct.pack('<BBH', set_speed, s2, cmd_s80)
                    CMDRSS3 = struct.pack('<BBH', set_speed, s3, cmd_s80)
                    ser.write(CMDLSS3)
                    ser.write(CMDRSS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDLS1 = struct.pack('<BBH', set_target, s2, cmd3)
                        CMDRS1 = struct.pack('<BBH', set_target, s3, cmd1)
                        ser.write(CMDLS1)
                        ser.write(CMDRS1)
                        time.sleep(1.2)
                        CMDLS3 = struct.pack('<BBH', set_target, s2, cmd1)
                        CMDRS3 = struct.pack('<BBH', set_target, s3, cmd3)
                        ser.write(CMDLS3)
                        ser.write(CMDRS3)
                        time.sleep(1.2)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDLS2 = struct.pack('<BBH', set_target, s2, cmd2)
                    CMDRS2 = struct.pack('<BBH', set_target, s3, cmd2)
                    ser.write(CMDLS2)
                    ser.write(CMDRS2)
                    ser.close()

            elif x == '3':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDES1 = struct.pack('<BBH', set_speed, s4, cmd_s20)
                    ser.write(CMDES1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s4, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.5)
                        CMDE3 = struct.pack('<BBH', set_target, s4, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.5)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s4, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDES2 = struct.pack('<BBH', set_speed, s4, cmd_s50)
                    ser.write(CMDES2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s4, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.3)
                        CMDE3 = struct.pack('<BBH', set_target, s4, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s4, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDES3 = struct.pack('<BBH', set_speed, s4, cmd_s80)
                    ser.write(CMDES3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s4, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.3)
                        CMDE3 = struct.pack('<BBH', set_target, s4, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s4, cmd2)
                    ser.write(CMDE2)
                    ser.close()

            elif x == '4':

                speed = raw_input("Please enter desired speed % :")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDES1 = struct.pack('<BBH', set_speed, s5, cmd_s20)
                    ser.write(CMDES1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s5, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.5)
                        CMDE3 = struct.pack('<BBH', set_target, s5, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.5)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s5, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDES2 = struct.pack('<BBH', set_speed, s5, cmd_s50)
                    ser.write(CMDES2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s5, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.3)
                        CMDE3 = struct.pack('<BBH', set_target, s5, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.3)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s5, cmd2)
                    ser.write(CMDE2)
                    ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDES3 = struct.pack('<BBH', set_speed, s5, cmd_s80)
                    ser.write(CMDES3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDE1 = struct.pack('<BBH', set_target, s5, cmd3)
                        ser.write(CMDE1)
                        time.sleep(1.2)
                        CMDE3 = struct.pack('<BBH', set_target, s5, cmd1)
                        ser.write(CMDE3)
                        time.sleep(1.2)
                        ser.close()

                    ser = serial.Serial('COM6')
                    CMDE2 = struct.pack('<BBH', set_target, s5, cmd2)
                    ser.write(CMDE2)
                    ser.close()

            elif x == '5':

                speed = raw_input('Please enter desired speed % :')

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDWPS1 = struct.pack('<BBH', set_speed, s6, cmd_s20)
                    ser.write(CMDWPS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWP1 = struct.pack('<BBH', set_target, s6, cmd1)
                        ser.write(CMDWP1)
                        time.sleep(1.5)
                        CMDWP3 = struct.pack('<BBH', set_target, s6, cmd3)
                        ser.write(CMDWP3)
                        time.sleep(1.5)
                        ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDWPS2 = struct.pack('<BBH', set_speed, s6, cmd_s50)
                    ser.write(CMDWPS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWP1 = struct.pack('<BBH', set_target, s6, cmd1)
                        ser.write(CMDWP1)
                        time.sleep(1.3)
                        CMDWP3 = struct.pack('<BBH', set_target, s6, cmd3)
                        ser.write(CMDWP3)
                        time.sleep(1.3)
                        ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDWPS3 = struct.pack('<BBH', set_speed, s6, cmd_s80)
                    ser.write(CMDWPS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWP1 = struct.pack('<BBH', set_target, s6, cmd1)
                        ser.write(CMDWP1)
                        time.sleep(1.2)
                        CMDWP3 = struct.pack('<BBH', set_target, s6, cmd3)
                        ser.write(CMDWP3)
                        time.sleep(1.2)
                        ser.close()

            elif x == '6':

                speed = raw_input("Please enter desired speed % : ")

                if speed == '20':

                    ser = serial.Serial('COM6')
                    CMDWRS1 = struct.pack('<BBH', set_speed, s7, cmd_s20)
                    ser.write(CMDWRS1)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWR1 = struct.pack('<BBH', set_target, s7, cmd1)
                        ser.write(CMDWR1)
                        time.sleep(1.0)
                        CMDWR3 = struct.pack('<BBH', set_target, s7, cmd3)
                        ser.write(CMDWR3)
                        time.sleep(1.0)
                        ser.close()

                elif speed == '50':

                    ser = serial.Serial('COM6')
                    CMDWRS2 = struct.pack('<BBH', set_speed, s7, cmd_s50)
                    ser.write(CMDWRS2)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWR1 = struct.pack('<BBH', set_target, s7, cmd1)
                        ser.write(CMDWR1)
                        time.sleep(0.6)
                        CMDWR3 = struct.pack('<BBH', set_target, s7, cmd3)
                        ser.write(CMDWR3)
                        time.sleep(0.6)
                        ser.close()

                elif speed == '80':

                    ser = serial.Serial('COM6')
                    CMDWRS3 = struct.pack('<BBH', set_speed, s7, cmd_s80)
                    ser.write(CMDWRS3)
                    ser.close()

                    end_time = time.time() + 10
                    while time.time() < end_time:
                        ser = serial.Serial('COM6')
                        ser.write('\xAA')
                        CMDWR1 = struct.pack('<BBH', set_target, s7, cmd1)
                        ser.write(CMDWR1)
                        time.sleep(0.35)
                        CMDWR3 = struct.pack('<BBH', set_target, s7, cmd3)
                        ser.write(CMDWR3)
                        time.sleep(0.35)
                        ser.close()

else:
    exit()

