import socket
# server_file.py
import sys
import os

# Add the parent folder to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import protocol

SERVER_IP = "127.0.0.1"
SERVER_PORT = 2223

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
client_msg = "testfile:awdasd,testfile2:fghfgsdff,testfile3:hrty,testfile4:rrswerf"
client_msg = protocol.add_length_to_message(client_msg)
client_socket.send(client_msg.encode())
server_response = protocol.get_msg(client_socket)
print(server_response)