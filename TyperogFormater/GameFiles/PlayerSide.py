import socket
import math

import time


s = socket.socket()
##URsim
host = '127.0.0.1'# IP of the robot
port = 12345

s.connect((host,port))

while True:
   ball_color = input()
   s.send(ball_color.encode())