#!/usr/bin/env python
import rospy
import socket
import time
import struct

from ur_feedback_info.msg import ur_information

def ur_signal_callback():

    pub = rospy.Publisher('ur_feedback', ur_information,queue_size=10)
    rospy.init_node('ur_talker', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz
    rospy.loginfo('The feedback signal from UR5')

    while not rospy.is_shutdown():
        Q1, Vq1, Pose1 = ur_tcp_comm()

        msg = ur_information()

        msg.name1 = "End effector Position"
        msg.X = Pose1[0]
        msg.Y = Pose1[1]
        msg.Z = Pose1[2]
        msg.Rx = Pose1[3]
        msg.Ry = Pose1[4]
        msg.Rz = Pose1[5]

        msg.name2 = "Joint position"
        msg.q1 = Q1[0]
        msg.q2 = Q1[1]
        msg.q3 = Q1[2]
        msg.q4 = Q1[3]
        msg.q5 = Q1[4]
        msg.q6 = Q1[5]

        msg.name3 = "Joint velocity"
        msg.vq1 = Vq1[0]
        msg.vq2 = Vq1[1]
        msg.vq3 = Vq1[2]
        msg.vq4 = Vq1[3]
        msg.vq5 = Vq1[4]
        msg.vq6 = Vq1[5]
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

def ur_tcp_comm():

    HOST = "192.168.1.102"  # The remote host
    PORT_30003 = 30003

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((HOST, PORT_30003))
    time.sleep(1.00)

    packet_1 = s.recv(4)
    packet_2 = s.recv(8)
    packet_3 = s.recv(48)
    packet_4 = s.recv(48)
    packet_5 = s.recv(48)
    packet_6 = s.recv(48)
    packet_7 = s.recv(48)

    packet_8_1 = s.recv(8)

    packet_8_1 = packet_8_1.encode("hex")
    q1 = str(packet_8_1)
    q1 = struct.unpack('!d', packet_8_1.decode('hex'))[0]

    packet_8_2 = s.recv(8)
    packet_8_2 = packet_8_2.encode("hex")
    q2 = str(packet_8_2)
    q2 = struct.unpack('!d', packet_8_2.decode('hex'))[0]

    packet_8_3 = s.recv(8)
    packet_8_3 = packet_8_3.encode("hex")
    q3 = str(packet_8_3)
    q3 = struct.unpack('!d', packet_8_3.decode('hex'))[0]

    packet_8_4 = s.recv(8)
    packet_8_4 = packet_8_4.encode("hex")
    q4 = str(packet_8_4)
    q4 = struct.unpack('!d', packet_8_4.decode('hex'))[0]

    packet_8_5 = s.recv(8)
    packet_8_5 = packet_8_5.encode("hex")
    q5 = str(packet_8_5)
    q5 = struct.unpack('!d', packet_8_5.decode('hex'))[0]

    packet_8_6 = s.recv(8)
    packet_8_6 = packet_8_6.encode("hex")
    q6 = str(packet_8_6)
    q6 = struct.unpack('!d', packet_8_6.decode('hex'))[0]

    packet_9_1 = s.recv(8)
    packet_9_1 = packet_9_1.encode("hex")
    vq1 = str(packet_9_1)
    vq1 = struct.unpack('!d', packet_9_1.decode('hex'))[0]

    packet_9_2 = s.recv(8)
    packet_9_2 = packet_9_2.encode("hex")
    vq2 = str(packet_9_2)
    vq2 = struct.unpack('!d', packet_9_2.decode('hex'))[0]

    packet_9_3 = s.recv(8)
    packet_9_3 = packet_9_3.encode("hex")
    vq3 = str(packet_9_3)
    vq3 = struct.unpack('!d', packet_9_3.decode('hex'))[0]

    packet_9_4 = s.recv(8)
    packet_9_4 = packet_9_4.encode("hex")
    vq4 = str(packet_9_4)
    vq4 = struct.unpack('!d', packet_9_4.decode('hex'))[0]

    packet_9_5 = s.recv(8)
    packet_9_5 = packet_9_5.encode("hex")
    vq5 = str(packet_9_5)
    vq5 = struct.unpack('!d', packet_9_5.decode('hex'))[0]

    packet_9_6 = s.recv(8)
    packet_9_6 = packet_9_6.encode("hex")
    vq6 = str(packet_9_6)
    vq6 = struct.unpack('!d', packet_9_6.decode('hex'))[0]

    packet_10 = s.recv(48)
    packet_11 = s.recv(48)

    packet_12 = s.recv(8)
    packet_12 = packet_12.encode("hex")
    x = str(packet_12)
    x = struct.unpack('!d', packet_12.decode('hex'))[0]

    packet_13 = s.recv(8)
    packet_13 = packet_13.encode("hex")
    y = str(packet_13)
    y = struct.unpack('!d', packet_13.decode('hex'))[0]

    packet_14 = s.recv(8)
    packet_14 = packet_14.encode("hex")
    z = str(packet_14)
    z = struct.unpack('!d', packet_14.decode('hex'))[0]

    packet_15 = s.recv(8)
    packet_15 = packet_15.encode("hex")
    Rx = str(packet_15)
    Rx = struct.unpack('!d', packet_15.decode('hex'))[0]

    packet_16 = s.recv(8)
    packet_16 = packet_16.encode("hex")
    Ry = str(packet_16)
    Ry = struct.unpack('!d', packet_16.decode('hex'))[0]

    packet_17 = s.recv(8)
    packet_17 = packet_17.encode("hex")
    Rz = str(packet_17)
    Rz = struct.unpack('!d', packet_17.decode('hex'))[0]

    Pose = [x * 1000, y * 1000, z * 1000, Rx*180.0/3.14, Ry*180.0/3.14, Rz*180.0/3.14]

    Q = [q1 * 180.0 / 3.14, q2 * 180.0 / 3.14, q3 * 180.0 / 3.14, q4 * 180.0 / 3.14, q5 * 180.0 / 3.14,
         q6 * 180.0 / 3.14]

    Vq = [vq1, vq2, vq3, vq4, vq5, vq6]

    return Q, Vq, Pose

if __name__ == '__main__':

    try:
        ur_signal_callback()
    except rospy.ROSInterruptException:
        pass





