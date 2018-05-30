
"""
 Python3 Vehicle collision simulator
 Sends a signal to a Fog node that a vehicle
 Has been involved in a collision

Created by: savavel
Last Edited: 10 May, 2018
"""


import socket
import time
import json

# Connect to the Fog Node
# in this case it's on localhost
host = 'localhost'
port = 1234
buf = 4096

# Create socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))

# Send a location and speed message
# to the Fog Node which will be registered
location = {'location': '43.2355,45.2245', 'speed': '75'}
clientsocket.send(json.dumps(location).encode("utf8"))
print("REPLY: " + clientsocket.recv(buf).decode("utf8").rstrip())
time.sleep(1);

"""
 Send a collision notification at
 the same location so vehicles
 in the vicinity are alerted
"""
collision = {'collision': '43.2355,45.2245', 'speed': '75'}
clientsocket.send(json.dumps(collision).encode("utf8"))
print("REPLY: " + clientsocket.recv(buf).decode("utf8").rstrip())

time.sleep(1);
# Disconnect from the Fog node
disconnect = {'disconnect': ''}
clientsocket.send(json.dumps(disconnect).encode("utf8"))
time.sleep(1);
